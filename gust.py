import requests
import time
import webbrowser
import os


def GREEN(text):
    print(f"\033[92m{text}\033[0m")

def YELLOW(text):
    print(f"\033[93m{text}\033[0m")

def RED(text):
    print(f"\033[91m{text}\033[0m")

def banner():
    GREEN("====== GENERIC URL SEARCH TOOL (YHG) ======")

def search_urls():
    try:
        while True:  
            num_urls = int(input("\nEnter the number of URLs to search (or 0 to exit): "))
            if num_urls == 0:
                GREEN("\nExiting the program. Goodbye!")
                break

            search_word = input("Enter the word to search for: ").strip()
            output_file = "results.txt"

            
            urls = []
            for i in range(num_urls):
                url = input(f"Enter URL {i + 1}: ").strip()
                urls.append(url)

            GREEN(f"\n[+] Starting search for '{search_word}' in {num_urls} URLs...\n")
            time.sleep(1)

            with open(output_file, "a") as file:  
                file.write(f"\n[Search Word: '{search_word}' | Time: {time.ctime()}]\n")
                file.write("=" * 50 + "\n")

                
                for i, url in enumerate(urls):
                    print(f"\n[+] Searching URL {i + 1}: {url}")
                    try:
                        
                        response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                        })

                        print(f"[DEBUG] URL: {url} | Status Code: {response.status_code}")

                        if response.status_code == 200:
                            
                            if search_word in response.text:
                                result = f"Match found in URL {i + 1}: {url}"
                                GREEN(result)
                                file.write(result + "\n")
                            else:
                                result = f"No match found in URL {i + 1}: {url}"
                                YELLOW(result)
                                file.write(result + "\n")
                        elif response.status_code == 404:
                            result = f"URL {i + 1} not found: {url}"
                            YELLOW(result)
                            file.write(result + "\n")
                        else:
                            result = f"Unexpected response for {url}: {response.status_code}"
                            RED(result)
                            file.write(result + "\n")
                    except requests.RequestException as e:
                        result = f"Error accessing {url}: {e}"
                        RED(result)
                        file.write(result + "\n")
                    time.sleep(1)  

                file.write("=" * 50 + "\n\n")

            GREEN("\nSearch complete! Results saved to 'results.txt'.\n")

            
            file_path = os.path.abspath(output_file)
            webbrowser.open(f"file://{file_path}")
    except ValueError:
        RED("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        RED("\nSearch interrupted by user. Exiting...")
        exit()

if __name__ == "__main__":
    banner()
    search_urls()
