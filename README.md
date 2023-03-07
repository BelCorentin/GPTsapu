# GPTsapu

This is the most basic python script to interact with GPT-3.5 turbo.

In order to make it work:

Create a conda env with openai installed 

replace the key string by your own OPENAI_API_KEY

```
echo 'export OPENAI_API_KEY=sk-RL5HBnS3VYnfaJanNOTATRUEKEYbkFJNPFODM0T4PK'  >> ~/.bashrc
```

```
alias gpt='conda activate openai && python /your/path/to/GPTsapu/gpt.py'
```
and just type in $ gpt !
