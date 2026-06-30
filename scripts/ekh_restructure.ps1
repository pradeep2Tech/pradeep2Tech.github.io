# Enterprise Knowledge Hub — one-time content restructure (pre-launch)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

function Move-Topic {
    param([string]$From, [string]$ToDir)
    $fromPath = $From
    if (-not $fromPath.EndsWith(".md")) { $fromPath = "$From.md" }
    $src = Join-Path $root $fromPath
    if (-not (Test-Path $src)) { Write-Warning "Skip missing: $fromPath"; return }
    $destDir = Join-Path $root $ToDir
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
    $name = Split-Path $src -Leaf
    $dest = Join-Path $destDir $name
    if (Test-Path $dest) { Write-Warning "Already exists: $dest"; return }
    Move-Item -Path $src -Destination $dest
    Write-Host "Moved $name -> $ToDir"
}

# --- Rename top-level sections ---
if (Test-Path "content/lld") {
    Move-Item "content/lld" "content/design-patterns"
    Write-Host "Renamed lld -> design-patterns"
}
if (Test-Path "content/java-cheatsheet") {
    Move-Item "content/java-cheatsheet" "content/java-engineering"
    Write-Host "Renamed java-cheatsheet -> java-engineering"
}

# --- Merge system-fundamentals into system-design ---
$sf = "content/system-fundamentals"
if (Test-Path $sf) {
    Get-ChildItem "$sf/*.md" | Where-Object { $_.Name -ne "_index.md" } | ForEach-Object {
        Move-Item $_.FullName "content/system-design/$($_.Name)"
    }
    Remove-Item $sf -Recurse -Force
    Write-Host "Merged system-fundamentals into system-design"
}

# --- Create handbook directories ---
@(
    "content/kafka-handbook",
    "content/kubernetes-handbook",
    "content/cloud-handbook",
    "content/database-handbook",
    "content/ai-for-engineers",
    "content/interview-prep",
    "content/spring-boot",
    "content/dsa-coding"
) | ForEach-Object {
    New-Item -ItemType Directory -Path $_ -Force | Out-Null
}

# --- Kafka handbook ---
$kafka = @(
    "kafka","rabbitmq","activemq","ibm-mq","nats","pulsar","sqs","sns",
    "google-pubsub","azure-service-bus","redpanda","module-messaging-streaming.md"
)
foreach ($t in $kafka) { Move-Topic "content/technology-playbook/$t" "content/kafka-handbook" }

# --- Kubernetes handbook ---
$k8s = @(
    "docker","podman","kubernetes","openshift","istio","linkerd","consul",
    "kong","nginx-api-gateway","traefik","ambassador","aws-api-gateway",
    "nginx-ingress","haproxy","traefik-ingress","prometheus","grafana",
    "elk-stack","opensearch-logging","loki","jaeger","zipkin","opentelemetry",
    "kubernetes-cronjobs","module-cloud-native.md"
)
foreach ($t in $k8s) { Move-Topic "content/technology-playbook/$t" "content/kubernetes-handbook" }

# --- Cloud handbook ---
$cloud = @(
    "eks","aks","gke","vault","aws-secrets-manager","azure-key-vault",
    "cloud-providers-comparison","aws-cloud","azure-cloud","gcp-cloud",
    "openshift-on-prem-kubernetes","module-cloud-providers.md"
)
foreach ($t in $cloud) { Move-Topic "content/technology-playbook/$t" "content/cloud-handbook" }

# --- Database handbook (selection from playbook) ---
$dbSelection = @(
    "postgresql","mysql","oracle","sql-server","mongodb","couchbase","cosmos-db",
    "cassandra","hbase","scylladb","redis","dynamodb","aerospike","neo4j",
    "amazon-neptune","influxdb","timescaledb","opentsdb","elasticsearch",
    "opensearch","solr","clickhouse","snowflake","bigquery","module-databases.md",
    "mongodb-vs-postgresql","cassandra-vs-mongodb","oracle-vs-postgresql",
    "clickhouse-vs-elasticsearch","elasticsearch-vs-opensearch","redis-vs-memcached"
)
foreach ($t in $dbSelection) { Move-Topic "content/technology-playbook/$t" "content/database-handbook" }

# --- Database internals merge ---
if (Test-Path "content/database-internals") {
    Get-ChildItem "content/database-internals/*.md" | Where-Object { $_.Name -ne "_index.md" } | ForEach-Object {
        $dest = "content/database-handbook/$($_.Name)"
        if (-not (Test-Path $dest)) { Move-Item $_.FullName $dest }
        else { Write-Warning "DB conflict: $($_.Name)" }
    }
    Remove-Item "content/database-internals" -Recurse -Force
    Write-Host "Merged database-internals into database-handbook"
}

# --- AI for engineers ---
$ai = @("milvus","pinecone","pgvector","weaviate","ai-vector-indexing-rag-scaling")
foreach ($t in $ai) {
    Move-Topic "content/technology-playbook/$t" "content/ai-for-engineers"
    Move-Topic "content/database-handbook/$t" "content/ai-for-engineers"
}

# --- Interview prep ---
$interview = @(
    "kafka-vs-rabbitmq","rest-vs-grpc","graphql-vs-rest","temporal-vs-airflow",
    "spark-vs-flink","kubernetes-vs-openshift","eks-vs-aks-vs-gke",
    "kong-vs-nginx-vs-aws-api-gateway","module-interview-preparation.md"
)
foreach ($t in $interview) { Move-Topic "content/technology-playbook/$t" "content/interview-prep" }

# --- Spring Boot ---
Move-Topic "content/technology-playbook/spring-batch.md" "content/spring-boot"

Write-Host "EKH restructure file moves complete."
