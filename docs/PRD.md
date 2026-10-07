# StudySpot — Mini PRD

**Owner:** Pranjal  
**Status:** MVP

## Problem
Students have several possible places to study, but the best location changes depending on whether they need silence, Wi-Fi, seating, or space for a group. Choosing often depends on scattered knowledge or trial and error.

## User
A college student deciding where to study on or near campus.

## Goal
Help a student get a reasonable study-location recommendation in under a minute.

## MVP requirements
- Ask about quiet, Wi-Fi, seating, and solo/group work.
- Rank a small dataset of study locations.
- Show one best match and several alternatives.
- Explain the recommendation in simple language.

## Not in MVP
Live occupancy, maps, login/accounts, reviews, reservations, and a complex ML model.

## Success metrics for a real test
- % of testers who say the recommendation is useful (4/5 or 5/5).
- % who would use the tool again.
- % who choose one of the recommended locations.

## Key product decision
I chose a transparent weighted recommendation system for the MVP. It is easier to debug and explain, and it lets me validate the user problem before investing in ML or live integrations.
