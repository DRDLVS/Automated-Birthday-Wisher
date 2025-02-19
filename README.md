# Birthday & Motivational Quote Email Automation

## Overview

This repository contains two Python scripts for automating email notifications:

### 1. Birthday Email Sender
- Reads a `birthdays.csv` file to check if today matches any birthday.
- Selects a random birthday letter template from the `letter_templates` folder.
- Replaces `[NAME]` in the template with the recipient's name.
- Sends a birthday email using an SMTP server.

### 2. Motivational Monday Quote Sender
- Checks if today is Monday.
- Reads motivational quotes from `quotes.txt`.
- Randomly selects a quote.
- Sends the selected quote via email using an SMTP server.

Both scripts automate email sending with personalized messages for birthdays and motivation at the start of the week.

