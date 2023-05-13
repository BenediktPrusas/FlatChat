from time import sleep

import openai
import streamlit as st
import configparser
import os

def init_open_ai()-> None:
    """
    Initialize OpenAI API key. If secrets.toml exists, read the key from there. Otherwise, use Streamlit secrets.
    """

    # Check if secrets.toml exists
    if os.path.isfile('.streamlit/secrets.toml'):
        # Read OPENAI_KEY from secrets.toml
        config = configparser.ConfigParser()
        config.read('.streamlit/secrets.toml')
        key = config.get('DEFAULT', 'OPENAI_KEY').strip('"')
        openai.api_key = key
    else:
        # Use Streamlit secrets if secrets.toml does not exist
        openai.api_key = st.secrets["DEFAULT"]["OPENAI_KEY"].strip('"')


def generate_intro(flat_description: str, personal_info: str, base_prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Concatenate given information and use it to generate a prompt for OpenAI's Chat API.

    Parameters:
    flat_description (str): Description of the flat.
    personal_info (str): Personal information to be included in the prompt.
    base_prompt (str): Base prompt for GPT-3.

    Returns:
    str: The generated text from GPT-3.
    """

    init_open_ai()

    # Send the prompt to GPT-3

    messages = [
        {"role": "system", "content": base_prompt},
        {"role": "user", "content": f"WG Anzeige: \n{flat_description}\n Persönliche Informationen: \n{personal_info}"},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    first_answer = response['choices'][0]['message']['content']

    # Return the generated text

    return first_answer


def generate_intro_self_improvement(flat_description: str, personal_info: str, base_prompt: str, model: str = "gpt-3.5-turbo") -> \
tuple[str, str, str]:
    """
    Concatenate given information and use it to generate a prompt for OpenAI's Chat API.

    Parameters:
    flat_description (str): Description of the flat.
    personal_info (str): Personal information to be included in the prompt.
    base_prompt (str): Base prompt for GPT-3.

    Returns:
    str: The generated text from GPT-3.
    """

    init_open_ai()

    # Send the prompt to GPT-3

    messages = [
        {"role": "system", "content": base_prompt},
        {"role": "user", "content": f"WG Anzeige: \n{flat_description}\n Persönliche Informationen: \n{personal_info}"},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    first_answer = response['choices'][0]['message']['content']

    # Return the generated text
    messages.append({"role": "assistant", "content": first_answer})
    messages.append({"role": "user", "content": "Kritisiere deinen vorgeschlagen text"})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    critic = response['choices'][0]['message']['content']
    print(critic)
    messages.append({"role": "assistant", "content": critic})
    messages.append(
        {"role": "user", "content": "Basierend auf deiner Kritik, verbessere deinen vorgeschlagen text"})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    second_answer = response['choices'][0]['message']['content']
    print(second_answer)
    return (second_answer, first_answer, critic)
