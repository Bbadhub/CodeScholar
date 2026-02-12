# Unseen: Advancing Digital Accessibility with Binaural Audio Technology in an Immersive Gaming Prototype

## Access

| Field | Value |
|-------|-------|
| DOI | `10.5753/jis.2025.4439` |
| Full Paper | [https://doi.org/10.5753/jis.2025.4439](https://doi.org/10.5753/jis.2025.4439) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1a83434dfee3cd9d0ea88c521f77bb507762480c](https://www.semanticscholar.org/paper/1a83434dfee3cd9d0ea88c521f77bb507762480c) |
| Source | [https://journalclub.io/episodes/unseen-advancing-digital-accessibility-with-binaural-audio-technology-in-an-immersive-gaming-prototype](https://journalclub.io/episodes/unseen-advancing-digital-accessibility-with-binaural-audio-technology-in-an-immersive-gaming-prototype) |
| Source | [https://www.semanticscholar.org/paper/1a83434dfee3cd9d0ea88c521f77bb507762480c](https://www.semanticscholar.org/paper/1a83434dfee3cd9d0ea88c521f77bb507762480c) |
| Year | 2026 |
| Citations | 1 |
| Authors | Claudia Susie C. Rodrigues, Vitória Nazareth, Ramon O. Azevedo, Priscyla Barbosa, Cláudia Werner |
| Paper ID | `cd2bf654-31a1-44f3-9f2d-6933b131c629` |

## Classification

- **Problem Type:** digital accessibility in gaming
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Digital Accessibility, Game Design
- **Technique:** Binaural Audio Technology
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents 'Unseen', a prototype game that utilizes binaural audio technology to create an immersive gaming experience for both sighted and visually impaired players. This approach is significant as it addresses the accessibility challenges in 3D gaming environments, allowing visually impaired individuals to engage in gameplay that is typically dominated by visual elements.

## Key Contribution

**The innovative use of binaural audio technology to create an inclusive gaming experience for visually impaired players.**

## Problem

The lack of accessible gaming experiences for blind and visually impaired individuals due to the visual-centric nature of most 3D games.

## Method

**Approach:** The method involves creating a 3D gaming environment where binaural audio serves as the primary feedback mechanism, allowing players to navigate and interact with the game world through sound. The game is designed to be equally engaging for both sighted and visually impaired players, promoting inclusivity.

**Algorithm:**

1. 1. Initialize the game environment in a 7x7 grid layout.
2. 2. Use binaural audio to provide spatial cues for player navigation.
3. 3. Allow player movement using keyboard inputs (WASD or arrow keys).
4. 4. Emit audio signals when the player approaches interactive objects.
5. 5. Provide audio descriptions and feedback based on player actions.
6. 6. Implement mini-games that utilize sound for gameplay mechanics.
7. 7. Conclude the game when the player solves the main puzzle.

**Input:** User keyboard inputs for movement and interaction; audio files for sound cues and descriptions.

**Output:** Audio feedback for navigation, clues, and game interactions; game completion status.

**Key Parameters:**

- `grid_size: 7x7`
- `audio_feedback_volume: adjustable`
- `interaction_sound: specific audio files for each object`

**Complexity:** not stated

## Benchmarks

**Tested on:** User testing with visually impaired and sighted participants

**Results:**

- User satisfaction, engagement levels, completion rates

**Compared against:** Traditional 3D games without accessibility features

**Improvement:** Not quantified in the paper.

## Implementation Guide

**Data Structures:** 7x7 grid for game layout, audio cue mapping for interactions

**Dependencies:** Unity Engine, Visual Studio 2019, Windows 10 Pro

**Core Operation:**

```python
while player is active: play audio cues based on position; if ENTER pressed: provide audio description or clue.
```

**Watch Out For:**

- Ensure audio feedback is clear and distinguishable.
- Test with both visually impaired and sighted users for balanced gameplay.
- Avoid overwhelming players with excessive audio cues.

## Use This When

- Developing games that require accessibility for visually impaired players.
- Creating immersive audio experiences in gaming.
- Designing educational games that promote inclusivity.

## Don't Use When

- Building purely visual games without audio components.
- Targeting audiences that do not require accessibility features.
- When the primary focus is on graphical fidelity over audio experience.

## Key Concepts

binaural audio, digital accessibility, game design, user interaction, inclusive gaming

## Connects To

- Sound Hunter (3D audio navigation)
- BlindSide (audio-only adventure games)
- The Vale: Shadow of the Crown (inclusive game design)

## Prerequisites

- Understanding of binaural audio principles.
- Familiarity with game development in Unity.
- Knowledge of accessibility standards in gaming.

## Limitations

- Requires players to use headphones for optimal experience.
- Limited to audio-based interactions, which may not appeal to all players.
- Development complexity increases with the need for extensive audio assets.

## Open Questions

- How can the approach be adapted for other disabilities?
- What additional features could enhance the immersive experience further?

## Abstract

For most 3D games, vision isn’t just part of the experience, it is the experience. The entire interface is built around it. Movement, interaction, feedback, and even storytelling are overwhelmingly visual. For blind and visually impaired players, this presents a near-total barrier to entry. You’re not just missing a few graphics. You’re missing the map, the Heads-Up Display, the cues that tell you where to go, what you’ve found, and what’s happening in the world around you. And while some mainstream games have certainly made some strides towards accessibility (offering features like screen reader support, audio menus, or controller vibration feedback) these adaptations tend to patch the edges, not solve the core problem. The player might be able to navigate a menu, but when the game drops them into a dynamic 3D environment, there’s no equivalent to spatial awareness, visual targeting, or ambient orientation. The player isn’t missing tools, they’re missing affordances without which, the sensory logic of the game breaks down. And that’s the central challenge the authors of today’s paper are trying to tackle.
