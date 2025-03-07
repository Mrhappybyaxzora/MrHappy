import openai

class LLM:
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

    def __init__(
            self,
            messages: list[dict[str, str]] = [],
            model: str = "gpt-3.5-turbo-1106",
            temperature: float = 0.0,
            system_prompt: str = "You are a helpful assistant.",
            max_tokens: int = 4096,
            verbose: bool = False,
            api_key: str | None = None
            ) -> None:
        """
        Initialize the LLM

        Parameters
        ----------
        messages : list[dict[str, str]], optional
            The list of messages, by default []
        model : str, optional
            The model to use, by default "gpt-3.5-turbo-1106"
        temperature : float, optional
            The temperature to use, by default 0.0
        system_prompt : str, optional
            The system prompt to use, by default ""
        max_tokens : int, optional
            The max tokens to use, by default 2048
        verbose : bool, optional
            The verbose to use, by default False
        api_key : str | None, optional
            The api key to use, by default None

        Examples
        --------
        >>> llm = LLM(api_key="your-openai-api-key")
        >>> llm.add_message("user", "Hello, how are you?")
        """
        assert api_key, "OpenAI API key is required"
        openai.api_key = api_key
        self.client = openai
        self.messages = messages
        self.model = model
        self.temperature = temperature
        self.system_prompt = system_prompt
        self.max_tokens = max_tokens
        self.verbose = verbose
        self.add_message(self.SYSTEM, self.system_prompt)

    def run(self, prompt: str) -> str:
        """
        Run the LLM

        Parameters
        ----------
        prompt : str
            The prompt to run

        Returns
        -------
        str
            The response

        Examples
        --------
        >>> llm.run("write python code to make a snake game")
        """
        self.add_message(self.USER, prompt)
        response = {
            "model": self.model,
            "messages": self.messages.copy(),
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        self.messages.pop()
        result = self.client.chat.completions.create(**response)
        content = result.choices[0].message.content
        
        if self.verbose:
            print(content)
            
        return content

    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the list of messages

        Parameters
        ----------
        role : str
            The role of the message
        content : str
            The content of the message

        Returns
        -------
        None

        Examples
        --------
        >>> llm.add_message("user", "Hello, how are you?")
        >>> llm.add_message("assistant", "I'm doing well, thank you!")
        """
        self.messages.append({"role": role, "content": content})

    def __getitem__(self, index) -> dict[str, str] | list[dict[str, str]]:
        """
        Get a message from the list of messages

        Parameters
        ----------
        index : int
            The index of the message to get

        Returns
        -------
        dict
            The message at the specified index

        Examples
        --------
        >>> llm[0]
        {'role': 'user', 'content': 'Hello, how are you?'}
        >>> llm[1]
        {'role': 'assistant', 'content': "I'm doing well, thank you!"}

        Raises
        ------
        TypeError
            If the index is not an integer or a slice
        """
        if isinstance(index, slice):
            return self.messages[index]
        elif isinstance(index, int):
            return self.messages[index]
        else:
            raise TypeError("Invalid argument type")

    def __setitem__(self, index, value) -> None:
        """
        Set a message in the list of messages

        Parameters
        ----------
        index : int
            The index of the message to set
        value : dict
            The new message

        Returns
        -------
        None

        Examples
        --------
        >>> llm[0] = {'role': 'user', 'content': 'Hello, how are you?'}
        >>> llm[1] = {'role': 'assistant', 'content': "I'm doing well, thank you!"}

        Raises
        ------
        TypeError
            If the index is not an integer or a slice
        """
        if isinstance(index, slice):
            self.messages[index] = value
        elif isinstance(index, int):
            self.messages[index] = value
        else:
            raise TypeError("Invalid argument type")

if __name__ == "__main__":
    from rich import print
    llm = LLM(api_key="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", system_prompt="You are an expert in Python.", max_tokens=40)
    llm.add_message("user", "Hello, how are you?")
    llm.add_message("assistant", "I'm doing well, thank you!")
    print(llm.run("write python code to make a snake game"))
