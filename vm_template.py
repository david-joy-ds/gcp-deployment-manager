COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'

def GenerateConfig(context):
  """Creates the first virtual machine."""

  resources = [{
      'name': 'the-first-vm',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': 'us-central1-f',
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/',context.env['project'],
                                  '/zones/us-central1-f/',
                                  'machineTypes/f1-micro']),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/','debian-cloud/global/','images/family/debian-9'])
              }
          }],
          'networkInterfaces': [{
              'network': '$(ref.my-network.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}