# Stickman World — Python / Panda3D starter

This is a first lightweight 3D prototype, not the finished game.

## Included
- Python 3D scene using Panda3D.
- Third-person follow camera.
- Simple humanoid assembled from 3D primitives.
- Neighborhood placeholders: mosque, home, cafe, shop and lesson-center.
- Keyboard movement and on-screen directional buttons.
- GitHub Actions workflow to build an Android App Bundle and convert it to a universal APK.

## GitHub build
1. Upload the **contents** of this ZIP to the root of a new GitHub repository. Do not nest the project inside another folder.
2. Open Actions and select **Build Stickman World APK**.
3. Choose **Run workflow** on `main`.
4. Download `StickmanWorld-APK` from Artifacts if the workflow succeeds.

No local Python, Godot or Android Studio installation is needed.

## Important
Panda3D Android packaging is a newer workflow and requires Python 3.13 and Android-specific Panda3D wheels. The GitHub workflow follows the published Panda3D packaging approach, but it has not been run in your repository; upstream wheels, SDK versions or packaging details may change and require fixes.
The APK uses a temporary debug key and is for testing only, not Play Store publishing.

Not implemented yet: online multiplayer, accounts, friend visits, chat, real prayer-time calculations and background reminders, actual Hayalhanem video playback, full female/male customization, complete interiors, economy/building progression and finished art/animation. The touch controls need testing on the target phone.
