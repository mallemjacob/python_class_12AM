from google import genai

client = genai.Client()


print('Enter a term to search:')
user_input = input()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=user_input
)
print(interaction.output_text)
