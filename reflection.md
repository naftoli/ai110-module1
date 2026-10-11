# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The hint says "go higher" when the number entered is higher than the secret number
2. The hint says "go lower" when the number entered is lower than the secret number
3. After putting in the corrent number, and then clicking on "New Game", nothing happens
4. The difficulty level doesn't increase per difficulty

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| entered 40 | hint - go higher | hint - go lower | the hint is reversed |
| entered 5 | hint - go lower | hint - go higher | the hint is reversed |
| clicked on "new game" | new game should start | nothing happens | You already won. Start a new game to play again. |
| changed level to "Hard" | there should be a LARGER range | the range became SMALLER | n/a |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I'm using Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked the AI: how come when i enter a lower number than expected it says "go higher"?
The AI answered: The hints are reversed in app.py’s check_guess: when your guess is greater than the secret, it says “Go HIGHER”; when it’s lower, it says “Go LOWER.” Those messages should be the opposite.
It's correct b/c when i fixed that it worked properly
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
One thing AI showed was the following:
Decimal guesses are silently truncated. logic_utils.py:38 converts values such as "42.9" to 42. Since this is a whole-number guessing game, it may be better to reject decimal input rather than turn it into a different guess.
Though it is a good point, I think a better solution would be to reject any non whole integer.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried it and i ran the tests as well as the added test
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the test for fix in difficulty level which can be found under test_difficulty.py
- Did AI help you design or understand any tests? How?
AI helped created the test based on the fix that it suggested which was correct
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
So the Streamlit app has an internal state that can be saved between reruns. it also has variables that get initialized each time it's ran. the session is 
kind of like Cookies / Session global variable in php.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would use AI to do most of the coding, but I would guide it on each step of the way.
- What is one thing you would do differently next time you work with AI on a coding task?
Make sure to have pointed clear instructions as oppose to vague ones.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code can be created extremely fast and efficiently provided the instructions are super clear and pointed. There also needs to be lots of tests
to ensure that the code is correct.