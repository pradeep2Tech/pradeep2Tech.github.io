/**
 * Global article accordion controller.
 *
 * Native <details> elements work automatically. Custom components can join the
 * same contract with `data-accordion` on the root and an element carrying
 * `aria-expanded` (optionally `data-accordion-trigger`) as their trigger.
 */
(function () {
  "use strict";

  const STORAGE_KEY = "accordionState";
  const ROOT_SELECTOR = "details, [data-accordion]";
  const TRIGGER_SELECTOR = "[data-accordion-trigger], [aria-expanded]";

  function rootsIn(article) {
    return Array.from(article.querySelectorAll(ROOT_SELECTOR));
  }

  function isOpen(root) {
    if (root instanceof HTMLDetailsElement) return root.open;
    const trigger = root.matches("[aria-expanded]") ? root : root.querySelector(TRIGGER_SELECTOR);
    return trigger?.getAttribute("aria-expanded") === "true";
  }

  function setOpen(root, open) {
    if (root instanceof HTMLDetailsElement) {
      root.open = open;
      return;
    }

    const trigger = root.matches("[aria-expanded]") ? root : root.querySelector(TRIGGER_SELECTOR);
    if (!trigger || isOpen(root) === open) return;

    // Clicking preserves the custom component's own animation and icon logic.
    if (typeof trigger.click === "function") trigger.click();
    else trigger.setAttribute("aria-expanded", String(open));
  }

  function storedPreference() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (_) {
      return null;
    }
  }

  function savePreference(value) {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch (_) {
      // Storage may be disabled; accordion controls still work normally.
    }
  }

  function setup(article) {
    const controls = article.querySelector("[data-accordion-controls]");
    if (!controls || controls.dataset.ready === "true") return;

    const expand = controls.querySelector('[data-accordion-action="expand"]');
    const collapse = controls.querySelector('[data-accordion-action="collapse"]');
    let preferenceApplied = false;

    function sync() {
      const roots = rootsIn(article);
      controls.hidden = roots.length === 0;
      if (!roots.length) return;

      if (!preferenceApplied) {
        preferenceApplied = true;
        const preference = storedPreference();
        if (preference === "expanded" || preference === "collapsed") {
          roots.forEach((root) => setOpen(root, preference === "expanded"));
        }
      }

      const openCount = roots.reduce((count, root) => count + Number(isOpen(root)), 0);
      expand.disabled = openCount === roots.length;
      collapse.disabled = openCount === 0;
    }

    function setAll(open) {
      rootsIn(article).forEach((root) => setOpen(root, open));
      savePreference(open ? "expanded" : "collapsed");
      sync();
    }

    expand.addEventListener("click", () => setAll(true));
    collapse.addEventListener("click", () => setAll(false));
    article.addEventListener("toggle", sync, true);
    article.addEventListener("click", () => requestAnimationFrame(sync));

    // Covers accordions produced after initial HTML parsing by current/future code.
    new MutationObserver(sync).observe(article, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ["open", "aria-expanded"]
    });

    controls.dataset.ready = "true";
    sync();
  }

  function init() {
    document.querySelectorAll("article.post-single").forEach(setup);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
