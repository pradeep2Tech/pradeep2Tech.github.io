# Fix internal links after EKH handbook split
$ErrorActionPreference = "Stop"
$root = "c:\Users\sach0725\projects\git_blogs\tech-blog"
Set-Location $root

$linkMap = @{
  '/technology-playbook/kafka-vs-rabbitmq/' = '/interview-prep/kafka-vs-rabbitmq/'
  '/technology-playbook/rest-vs-grpc/' = '/interview-prep/rest-vs-grpc/'
  '/technology-playbook/graphql-vs-rest/' = '/interview-prep/graphql-vs-rest/'
  '/technology-playbook/temporal-vs-airflow/' = '/interview-prep/temporal-vs-airflow/'
  '/technology-playbook/spark-vs-flink/' = '/interview-prep/spark-vs-flink/'
  '/technology-playbook/kubernetes-vs-openshift/' = '/interview-prep/kubernetes-vs-openshift/'
  '/technology-playbook/eks-vs-aks-vs-gke/' = '/interview-prep/eks-vs-aks-vs-gke/'
  '/technology-playbook/kong-vs-nginx-vs-aws-api-gateway/' = '/interview-prep/kong-vs-nginx-vs-aws-api-gateway/'
  '/technology-playbook/mongodb-vs-postgresql/' = '/database-handbook/mongodb-vs-postgresql/'
  '/technology-playbook/cassandra-vs-mongodb/' = '/database-handbook/cassandra-vs-mongodb/'
  '/technology-playbook/oracle-vs-postgresql/' = '/database-handbook/oracle-vs-postgresql/'
  '/technology-playbook/clickhouse-vs-elasticsearch/' = '/database-handbook/clickhouse-vs-elasticsearch/'
  '/technology-playbook/elasticsearch-vs-opensearch/' = '/database-handbook/elasticsearch-vs-opensearch/'
  '/technology-playbook/redis-vs-memcached/' = '/database-handbook/redis-vs-memcached/'
  '/technology-playbook/aws-cloud/' = '/cloud-handbook/aws-cloud/'
  '/technology-playbook/azure-cloud/' = '/cloud-handbook/azure-cloud/'
  '/technology-playbook/gcp-cloud/' = '/cloud-handbook/gcp-cloud/'
  '/technology-playbook/openshift-on-prem-kubernetes/' = '/cloud-handbook/openshift-on-prem-kubernetes/'
  '/technology-playbook/cloud-providers-comparison/' = '/cloud-handbook/cloud-providers-comparison/'
  '/technology-playbook/eks/' = '/cloud-handbook/eks/'
  '/technology-playbook/aks/' = '/cloud-handbook/aks/'
  '/technology-playbook/gke/' = '/cloud-handbook/gke/'
  '/technology-playbook/vault/' = '/cloud-handbook/vault/'
  '/technology-playbook/aws-secrets-manager/' = '/cloud-handbook/aws-secrets-manager/'
  '/technology-playbook/azure-key-vault/' = '/cloud-handbook/azure-key-vault/'
  '/technology-playbook/kafka/' = '/kafka-handbook/kafka/'
  '/technology-playbook/spring-batch/' = '/spring-boot/spring-batch/'
  '/technology-playbook/pgvector/' = '/ai-for-engineers/pgvector/'
  '/technology-playbook/milvus/' = '/ai-for-engineers/milvus/'
  '/technology-playbook/pinecone/' = '/ai-for-engineers/pinecone/'
  '/technology-playbook/weaviate/' = '/ai-for-engineers/weaviate/'
}

$dbTopics = @('postgresql','mysql','oracle','sql-server','mongodb','couchbase','cosmos-db','cassandra','hbase','scylladb','redis','dynamodb','aerospike','neo4j','amazon-neptune','influxdb','timescaledb','opentsdb','elasticsearch','opensearch','solr','clickhouse','snowflake','bigquery')
foreach ($t in $dbTopics) { $linkMap["/technology-playbook/$t/"] = "/database-handbook/$t/" }

$k8sTopics = @('docker','podman','kubernetes','openshift','istio','linkerd','consul','kong','nginx-api-gateway','traefik','ambassador','aws-api-gateway','nginx-ingress','haproxy','traefik-ingress','prometheus','grafana','elk-stack','opensearch-logging','loki','jaeger','zipkin','opentelemetry','kubernetes-cronjobs')
foreach ($t in $k8sTopics) { $linkMap["/technology-playbook/$t/"] = "/kubernetes-handbook/$t/" }

$kafkaTopics = @('rabbitmq','activemq','ibm-mq','nats','pulsar','sqs','sns','google-pubsub','azure-service-bus','redpanda')
foreach ($t in $kafkaTopics) { $linkMap["/technology-playbook/$t/"] = "/kafka-handbook/$t/" }

$files = Get-ChildItem -Recurse -Include *.md,*.html -File | Where-Object { $_.FullName -notmatch '\\themes\\' }
foreach ($file in $files) {
  $text = [IO.File]::ReadAllText($file.FullName)
  $orig = $text
  foreach ($k in $linkMap.Keys) { $text = $text.Replace($k, $linkMap[$k]) }
  if ($text -ne $orig) { [IO.File]::WriteAllText($file.FullName, $text) }
}
Write-Host "Handbook link fixes complete."
