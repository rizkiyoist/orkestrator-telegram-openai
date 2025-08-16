# modifikasi dari https://github.com/openai/openai-python originally licensed under Apache-2.0
#
# Copyright (c) Rizki Hadiaturrasyid
#

import os
from openai import OpenAI

client = OpenAI(
    api_key="your key here",
    base_url="https://openrouter.ai/api/v1",
)


response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[
        {"role": "developer", "content": "Anda adalah asisten Orkestrator AI."},
        {
            "role": "user",
            "content": "Siapa kamu?",
        },
    ],
)

print(response.choices[0].message.content)