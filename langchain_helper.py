from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableMap
from openai_key import openapi_key
import os

os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Define prompts
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma-separated list."
    )

    # Create a runnable sequence
    chain = RunnableSequence(
        RunnableMap({"restaurant_name": prompt_template_name | llm}),
        lambda inputs: {
            "restaurant_name": inputs["restaurant_name"],
            "menu_items": llm.invoke(
                prompt_template_items.format(restaurant_name=inputs["restaurant_name"])
            )
        }
    )

    # Run the chain
    response = chain.invoke({"cuisine": cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items('indian'))