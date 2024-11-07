# Commit GPT

---

Generate a commit message for a git repository using the LLM of your choice.

> [!NOTE]
> The starter project assumes you're using a LLM that follows the OpenAI API format.
> For documentation of the OpenAI API format, see [here](https://platform.openai.com/docs/api-reference/introduction).

---

## Installation

Install the dependencies using `pip install -r requirements.txt`.

---

## Usage

```bash
python main.py <path-to-git-repository>
```

## Example

```bash
python main.py .
```

Output:

```bash
Suggested commit message:
Title: Configure Constants
Description: Filled in MODEL_NAME and API_ENDPOINT with specific values
```
