# PowerShell helper — generate handbook list/single layouts
$sections = @(
  @{ slug = "kafka-handbook"; modules = "kafka_handbook_modules"; order = "kafka_handbook_order"; label = "Kafka Handbook" },
  @{ slug = "kubernetes-handbook"; modules = "kubernetes_handbook_modules"; order = "kubernetes_handbook_order"; label = "Kubernetes Handbook" },
  @{ slug = "cloud-handbook"; modules = "cloud_handbook_modules"; order = "cloud_handbook_order"; label = "Cloud Handbook" },
  @{ slug = "database-handbook"; modules = "database_handbook_modules"; order = "database_handbook_order"; label = "Database Handbook" },
  @{ slug = "ai-for-engineers"; modules = "ai_for_engineers_modules"; order = "ai_for_engineers_order"; label = "AI for Engineers" },
  @{ slug = "interview-prep"; modules = "interview_prep_modules"; order = "interview_prep_order"; label = "Interview Preparation" },
  @{ slug = "spring-boot"; modules = "spring_boot_modules"; order = "spring_boot_order"; label = "Spring Boot Handbook" },
  @{ slug = "dsa-coding"; modules = "dsa_coding_modules"; order = "dsa_coding_order"; label = "DSA & Coding" }
)

$listTpl = @'
{{- define "main" -}}
{{- partial "curriculum-module-list.html" (dict "page" . "section" "SLUG" "modulesData" "MODULES" "navPartial" "section-nav.html" "tocLabel" "LABEL table of contents") -}}
{{- end -}}
'@

$singleTpl = @'
{{- define "main" -}}
{{- partial "curriculum-section-single.html" (dict "page" . "navPartial" "section-nav.html" "orderData" "ORDER" "section" "SLUG") -}}
{{- end -}}
'@

foreach ($s in $sections) {
  $dir = "layouts/$($s.slug)"
  New-Item -ItemType Directory -Path $dir -Force | Out-Null
  ($listTpl -replace 'SLUG', $s.slug -replace 'MODULES', $s.modules -replace 'LABEL', $s.label) | Set-Content "$dir/list.html" -Encoding UTF8
  ($singleTpl -replace 'SLUG', $s.slug -replace 'ORDER', $s.order) | Set-Content "$dir/single.html" -Encoding UTF8
}

Write-Host "Handbook layouts created."
