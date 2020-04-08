def GenerateConfig(context):

    resources = [{
        'name': 'my-network',
        'type': 'compute.v1.network',
        'properties': {
            'routingConfig': {
                'routingMode': 'REGIONAL',
                'autoCreateSubnetworks': 'true'
            }
        }
    }]
    
    return {'resources': resources}
