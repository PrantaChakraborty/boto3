import boto3

access_key = ''
secret_access_key = ''


def get_all_clusters():
    ecs_client = boto3.client('ecs', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)
    response = ecs_client.list_clusters()
    cluster_arns = response['clusterArns']
    return cluster_arns

# print(get_all_regions())
# Get all clusters
clusters = get_all_clusters()
print(clusters)

# Print the clusters
for cluster_arn in clusters:
    print(cluster_arn)