# Newsletter

An email to her list, sent through MCM. Not a social platform, but it follows the same switch: on only when the platforms line in her strategy names it.

## When to recommend it
When she sells something people decide on over time (coaching, a program, a course, consulting, a service with a long consideration), or when she already has a list of past clients and leads. Not as a first step for someone with no contacts at all: say the list grows from her forms and bookings in MCM, and start when it has people on it.

## Account
Her sending address in MCM (a verified domain, so emails don't land in spam) and her list: a tag or a segment in MCM. Both live in `ghl.md` under **Newsletter**: from name, from email, reply-to, list. Deliverability (the domain, its records) and the list are part of her MCM build; the content setup records the details as she gives them and doesn't check them.

## Formats
From the strategy library's newsletter catalog: one-idea letter (default), story and lesson, client question, case study, her week. About one issue in four or five is an **offer issue**: same format, but the one ask is the sale.

## Caption
The newsletter is its own writing, from the playbook's newsletter section:
1. Plain text. No images, no designed template. It should read like an email from a person.
2. 200-400 words. One idea, short paragraphs, white space.
3. Open with a moment, not a greeting paragraph. "Oi <first name>," then straight in. Written in Brazilian Portuguese.
4. One CTA: reply, book, or one link. A question they can reply to counts, and replies are the best signal.
5. Subject: 2-3 options, short and specific (about 3-7 words), written last, no emoji, no clickbait. A question is fine when it's a real one.
6. Preview text: one line that adds to the subject, never repeats it.
7. Sign off as her, by first name.

## Scheduling
MCM `create-email-campaign` with `editorType: text`, then `schedule-campaign` with `scheduleType: scheduled`, `sendAt` in her time zone, `emailMeta` (subject, from name, from email, reply-to, preview text) and `recipients` = the list from `ghl.md`. Default cadence: every two weeks for a new list, weekly once she's keeping up; default day and time: Tuesday morning in her time zone. A newsletter doesn't count toward the one-post-a-day rule: email and social are separate channels. When the newsletter leads the theme, it's written by 2 days before it's sent, and it sets the topic for the posts until the next issue.

## Results
Clicks, replies and unsubscribes per issue. Opens are recorded but not trusted (Apple Mail inflates them). A small list engages more; judge over two to three months, not one issue. Unsubscribes above about 1% of the list on an issue are worth a look at that issue's topic.
