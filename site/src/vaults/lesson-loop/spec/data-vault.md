# A player's data vault

```
record/
  profile.json          the player, their level, their themes
  lessons/              one file per lesson: the memo transcript and the note
  matches/              one file per match note
  clips/                clips, and what the agent pulled out of them
  briefings/            briefings, each for a named coach and date
  record.json           the timeline the app reads
```

Keys: the player holds the vault key. Each coach gets a read key and an append token for their own lane. Clubs get nothing by default. The app vault holds no player data at all.
