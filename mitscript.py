import subprocess

#Defining Functions

def main():
    selection = float(input("\n\nSelect the mitigation you want to run by inputing the coressponding number:\n\n1. Flow Logs Disabled\n2. Flow Logs Disabled ALL Regions\n3. Bucket Logs Disabled\n4. Shielded VM Disabled\n5. Public IP Address\n6. Bucket policy only disabled\n7. Private google access disabled\n8. Bucket IAM not monitored\n9. Open RDP port\n10. Default network\n11. Default service account used\n12. DNS logging disabled\n\nValue: "))

    if selection == 1:
        flowlogsfunct();
        morework();
    elif selection == 2:
        flowlogsallfunct();
        morework();
    elif selection == 3:
        bucketfunct();
        morework();
    elif selection == 4:
        shieldedvmfunct();
        morework();
    elif selection == 5:
        publicipfunct();
        morework();
    elif selection == 6:
        bucketuniformfunct();
        morework();
    else:
        print('Not Valid Input');

def morework():
    answer = input('Do You Wish to Perform More Mitigations? y/n\n')
    if answer == 'y':
        main();
    else:
        print('Thank You! Go OneCloud!');

def flowlogsfunct():
    subnet_name = input('What is the name of the Subnet?\n')
    region = input('What is the region?\n');
    subprocess.run(['gcloud', 'compute', 'networks', 'subnets', 'update', f'{subnet_name}', '--enable-flow-logs', f'--region={region}']);
    print("Done!");

def flowlogsallfunct():
    regions = ['us-central1', 'asia-northeast3', 'europe-west1', 'us-east4', 'europe-west2', 'europe-west6', 'us-east1', 'asia-northeast1', 'asia-east2', 'us-west1', 'australia-southeast1', 'us-west3', 'asia-east1', 'me-west1', 'asia-south1', 'southamerica-east1', 'us-east5', 'us-south1', 'southamerica-west1', 'europe-west8', 'europe-west3', 'europe-west4', 'australia-southeast2', 'europe-north1', 'asia-south2', 'europe-central2', 'us-west4', 'asia-southeast2', 'europe-southwest1', 'asia-northeast2', 'northamerica-northeast1', 'northamerica-northeast2', 'asia-southeast1', 'us-west2', 'europe-west9']
    subnet = input('What is the name of the subnet?\n');
    for i in regions:
        subprocess.run(['gcloud', 'compute', 'networks', 'subnets', 'update', f'{subnet}', '--enable-flow-logs', f'--region={i}']);
    print("Done!");

def bucketfunct():
    bucket = input('What is the bucket that was added? Including: gs://\n');
    subprocess.run(['gcloud', 'storage', 'buckets', 'update', f'{bucket}', f'--log-bucket={bucket}']);
    print("Done!");

def shieldedvmfunct():
    vmname = input('What is the name of the VM?\n');
    zone = input('What Zone is VM in? ex. us-east1-b\n');
    subprocess.run(['gcloud', 'compute', 'instances', 'stop', f'{vmname}', f'--zone={zone}']);
    subprocess.run(['gcloud', 'compute', 'instances', 'update', f'{vmname}', f'--zone={zone}', '--shielded-secure-boot']);
    subprocess.run(['gcloud', 'compute', 'instances', 'start', f'{vmname}', f'--zone={zone}']);
    print("Done!");

def publicipfunct():
    print('This wizard will help you remove Public IP addresses from Virtual Machinces. NOTE: This will only work on access configs with default names if for some reason the name has been customized this script will fail.')
    vmname = input('What is the Name of the VM?\n')
    zone = input('What is the Zone that the VM is in?\n')
    subprocess.run(['gcloud', 'compute', 'instances', 'delete-access-config', f'{vmname}', f'--zone={zone}', '--access-config-name', 'External NAT']);
    print("Done!");

def bucketuniformfunct():
    bucket = input('What is the name of the bucket? Note: Do not include gs://');
    subprocess.run(['gsutil', 'bucketpolicyonly', 'set', 'on', f'gs://{bucket}']);
    print("Done!");

#Program Call
main();
    
