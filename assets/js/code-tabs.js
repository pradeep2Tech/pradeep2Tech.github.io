(function () {
  function activateCodeTab(tabsRoot, lang) {
    const targetLang = lang || tabsRoot.dataset.codeDefault || tabsRoot.dataset.implDefault || "java";

    tabsRoot.querySelectorAll(".code-tab-btn, .impl-tab-btn").forEach((btn) => {
      const selected = btn.dataset.tab === targetLang;
      btn.setAttribute("aria-selected", selected ? "true" : "false");
      btn.tabIndex = selected ? 0 : -1;
    });

    tabsRoot.querySelectorAll(".code-tab-panel, .impl-tab-panel").forEach((panel) => {
      const panelLang = panel.dataset.codeTab || panel.dataset.implTab;
      const active = panelLang === targetLang;
      panel.classList.toggle("is-active", active);
      if (active) {
        panel.removeAttribute("hidden");
      } else {
        panel.setAttribute("hidden", "");
      }
    });
  }

  function initCodeTabs(root) {
    if (root.dataset.codeTabsReady === "true") return;
    root.dataset.codeTabsReady = "true";
    const defaultLang = root.dataset.codeDefault || root.dataset.implDefault || "java";
    activateCodeTab(root, defaultLang);
  }

  window.initCodeTabs = function () {
    document.querySelectorAll("[data-code-tabs], [data-impl-tabs]").forEach(initCodeTabs);
  };

  // Backward-compatible alias used by extend_footer.html
  window.initImplTabs = window.initCodeTabs;

  document.addEventListener("click", (e) => {
    const btn = e.target.closest(".code-tab-btn, .impl-tab-btn");
    if (!btn) return;
    const root = btn.closest("[data-code-tabs], [data-impl-tabs]");
    if (!root) return;
    e.preventDefault();
    activateCodeTab(root, btn.dataset.tab);
  });

  document.addEventListener("keydown", (e) => {
    const btn = e.target.closest(".code-tab-btn, .impl-tab-btn");
    if (!btn) return;
    const bar = btn.closest(".code-tabs-bar, .impl-tabs-bar");
    const root = btn.closest("[data-code-tabs], [data-impl-tabs]");
    if (!bar || !root) return;
    const tabs = Array.from(bar.querySelectorAll(".code-tab-btn, .impl-tab-btn"));
    const current = tabs.indexOf(btn);
    if (e.key === "ArrowRight") {
      e.preventDefault();
      tabs[(current + 1) % tabs.length].focus();
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      tabs[(current - 1 + tabs.length) % tabs.length].focus();
    } else if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      activateCodeTab(root, btn.dataset.tab);
    }
  });
})();
