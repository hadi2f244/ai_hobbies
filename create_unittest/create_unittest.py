from openai import OpenAI
import sys

from function_source_extractor import get_function_source

## Openai
#openai.api_key = 'your-api-key'
# client = OpenAI(api_key=openai.api_key)
model="gpt-3.5-turbo"

## Lmstudio
base_url = "http://localhost:1234/v1" # point to the local server
api_key = "not-needed" # no need for an API key
client = OpenAI(api_key=api_key, base_url= base_url)
model="local-model"

def generate_test_cases(requirement):
    global model
    response = client.chat.completions.create(
      # temperature=0.8,
      # max_tokens=1500,
      # top_p=1.0,
      # frequency_penalty=0.0,
      # presence_penalty=0.0,
      model=model,
      messages=[
        {"role": "system", "content": "You are a helpful assistant capable of generating software test cases. Return only the code in the completion. I don't want any other comments. Don't say 'here is your code' or similar remarks."},
        {"role": "user", "content": requirement}
      ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_unittest.py file_path function_name number_of_unitest")
    else:
        file_path = sys.argv[1]  # The file path is the first argument
        function_name = sys.argv[2]  # The function name is the second argument
        unit_test_numbers = sys.argv[3]

        # Get function
        # file_path = './test.py'
        # function_name = 'multiply2'
        source_code = get_function_source(file_path, function_name)
        if source_code:
            print("Extracted function source code:\n", source_code)
        else:
            print("Function not found.")

        print("Progressing ...\r\n\r\n")

        requirement = "Write " + unit_test_numbers +  " diffrent unittest for this python function:\n"+ "'''"+ source_code +"'''."
        test_cases = generate_test_cases(requirement)
        print(test_cases)

