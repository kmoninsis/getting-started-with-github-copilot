Getting Started with GitHub Copilot

👋 Hey there @sushanshetty2601-pixel! Welcome to your Skills exercise!

Welcome to the exciting world of GitHub Copilot! 🚀 In this exercise, you'll unlock the potential of this AI-powered coding assistant to accelerate your development process. Let's dive in and have some fun exploring the future of coding together! 💻✨

✨ This is an interactive, hands-on GitHub Skills exercise!

As you complete each step, I’ll leave updates in the comments:

✅ Check your work and guide you forward
💡 Share helpful tips and resources
🚀 Celebrate your progress and completion
Let’s get started - good luck and have fun!

— Mona

If you encounter any issues along the way please report them here.

Activity
github-actions
github-actions commented 50 minutes ago
github-actions
bot
50 minutes ago – with GitHub Actions
Contributor
Author
Step 1: Hello Copilot
Welcome to your "Getting Started with GitHub Copilot" exercise! 🤖

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities. 🎻 ⚽️ ♟️

screenshot of Mergington High School WebApp

📖 Theory: Getting to know GitHub Copilot
copilot logo

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.

As you work in your IDE, you'll most often interact with GitHub Copilot in the following ways:

Interaction Mode	📝 Description	🎯 Best For
⚡ Inline suggestions	AI-powered code suggestions that appear as you type, offering context-aware completions from single lines to entire functions.	Completion of the current line, sometimes a whole new block of code
💭 Inline Chat	Interactive chat scoped to your current file or selection. Ask questions about specific code blocks.	Code explanations, debugging specific functions, targeted improvements
💬 Ask Mode	Optimized for answering questions about your codebase, coding, and general technology concepts.	Understanding how code works, brainstorming ideas, asking questions
🤖 Agent Mode	Recommended default mode for most coding tasks: autonomous edits, tool use, and follow-through until the task is done.	Daily coding tasks, from scoped fixes to larger multi-file implementation work
🧭 Plan Agent	Optimized for drafting a plan and asking clarifying questions before any code changes are made.	When you want a reviewed plan first, then hand off to implementation
As you work, you'll find GitHub Copilot can help out in several places across the github.com website and in your favorite coding environments such as VS Code, Jet Brains, and Xcode!

For today's coding though, we will practice with VS Code in a pre-configured development environment known as a GitHub Codespace.

Tip

You can learn more about current and upcoming features in the GitHub Copilot Features documentation.

⌨️ Activity: Get a project intro from Copilot Chat
Let's start up our development environment, use copilot to learn a bit about the project, and then give it a test run.

Use the below button to open the Create Codespace page in a new tab. Use the default configuration.

Open in GitHub Codespaces

Confirm the Repository field is your copy of the exercise, not the original, then click the green Create Codespace button.

✅ Your copy: /sushanshetty2601-pixel/skills-getting-started-with-github-copilot
❌ Original: /skills/getting-started-with-github-copilot
Wait a moment for Visual Studio Code to load in your browser.

In the left sidebar, click the extensions tab and verify that the GitHub Copilot and Python extensions are installed and enabled.

copilot extension for VS Code python extension for VS Code
At the top of VS Code, locate and click the Toggle Chat icon to open a Copilot Chat side panel.

image
🪧 Note: If this is your first time using GitHub Copilot, you will need to accept the usage terms to continue.

Make sure you are in Ask Mode for our first interaction

screenshot showing Ask Mode selection in Copilot Chat
Enter the below prompt to ask Copilot to introduce you to the project.

Static Badge

@workspace Please briefly explain the structure of this project.
What should I do to run it?
🪧 Note: It is not necessary to follow Copilot's recommended instructions. We have already prepared the environment for you.

What is @workspace?
Now that we know a bit more about the project, let's actually try running it! In the left sidebar, select the Run and Debug tab and then press the Start Debugging icon.

image
We want to see our webpage running in a browser, so let's find the url and port. If it isn't visible, expand the lower panel and select the Ports tab.

In the list, find port 8000 and the related link. Hover over the link and select the Open in browser icon.

image

⌨️ Activity: Use Copilot to help remember a terminal command 🙋
Great work! Now that we are familiar with the app and we know it works, let's ask copilot for help starting a branch so we can do some customizing.

In VS Code's bottom panel, select the Terminal tab and on the right side click the plus + sign to create a new terminal window.

🪧 Note: This will avoid stopping the existing debug session that is hosting our web application service.

Within the new terminal window use the keyboard shortcut Ctrl + I (windows) or Cmd + I (mac) to bring up Copilot's Terminal Inline Chat.

Let's ask Copilot to help us remember a command we have forgotten: creating a branch and publishing it.

Static Badge

Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
💡 Tip: If Copilot doesn't give you quite what you want, you can always continue explaining what you need. Copilot will remember the conversation history for follow-up responses.

Press the Run button to let Copilot insert the terminal command for us. No need to copy and paste!

After a moment, look in the VS Code lower status bar, on the left, to see the active branch. It should now say accelerate-with-copilot. If so, you are all done with this step!

Now that your branch is pushed to GitHub, Mona should already be busy checking your work. Give her a moment and keep watch in the comments. You will see her respond with progress info and the next lesson.

Having trouble? 🤷

If you don't get feedback, here are some things to check:

Make sure your created the branch with the exact name accelerate-with-copilot. No prefixes or suffixes.
Make sure the branch was indeed published to your repository.
github-actions
github-actions commented 50 minutes ago
github-actions
bot
50 minutes ago – with GitHub Actions
Contributor
Author

Please, follow the steps above.
I'll watch your progress in the background to provide feedback. 🧐