.. py:currentmodule:: asyncakinator



Quick Examples
==============

Here is a quick example of how to use the library.

.. code-block:: python

    import akinator
    import asyncio

    aki = akinator.Akinator(
        language=akinator.Language.ENGLISH,
        theme=akinator.Theme.ANIMALS,
    )

    async def main():
        question = await aki.start()

        while aki.progression <= 80:
            a = input(f"{question}\n\t")
            if a == "b":
                try:
                    question = await aki.back()
                except akinator.CantGoBackAnyFurther:
                    continue
            else:
                try:
                    question = await aki.answer(akinator.Answer.from_str(a))
                except akinator.InvalidAnswer:
                    print("Invalid answer. Please try again.\n")
                    continue
        await aki.win()

        correct = input(
            f"You are thinking of {aki.first_guess.name} ({aki.first_guess.description}). "
            f"Am I correct?\n{aki.first_guess.absolute_picture_path}\n\t"
        )
        if akinator.Answer.from_str(correct) == akinator.Answer.YES:
            print("Nice.")
        else:
            print("Maybe next time.")
        await aki.close()

    asyncio.run(main())