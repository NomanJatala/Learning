# Roadmap: From Python + ML to Autonomous Decision-Making AI

**Target field:** perception, prediction, and control systems for autonomous vehicles / decision-making robots
**Starting point:** Python + learning ML
**Realistic timeline:** 12–18 months at ~10–15 hrs/week

> Links come from the roadmap PDF where it gave them. YouTube playlists and a few other URLs were looked up and verified separately. Where a link points to an older course edition, it is marked in the table. If a URL is dead, search by the resource name.

---

## Phase 0 — Math (4–6 weeks)

| Course / Resource | Link / Source |
|---|---|
| 3Blue1Brown — Essence of Linear Algebra | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab |
| MIT OCW 18.06 Linear Algebra (Gilbert Strang) | https://ocw.mit.edu |
| Harvard Stat 110 — Probability (Joe Blitzstein), course site | https://stat110.hsites.harvard.edu/ |
| Harvard Stat 110 — YouTube lectures | https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo |

**Proof:** explain gradient, eigenvector, and conditional probability geometrically.

## Phase 1 — Core Machine Learning (4–6 weeks)

| Course / Resource | Link / Source |
|---|---|
| Machine Learning Specialization (Andrew Ng, DeepLearning.AI) — audit free on Coursera | https://www.deeplearning.ai/courses/machine-learning-specialization/ |
| Stanford CS229 (harder alternative) | https://cs229.stanford.edu |
| Kaggle Learn micro-courses + a real competition (Titanic / House Prices) | https://www.kaggle.com/learn |

**Proof:** build and evaluate a model from scratch on a tabular dataset.

## Phase 2 — Deep Learning Core (6–8 weeks)

| Course / Resource | Link / Source |
|---|---|
| fast.ai — Practical Deep Learning for Coders | https://course.fast.ai |
| Andrej Karpathy — Neural Networks: Zero to Hero (YouTube) | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ |
| Andrej Karpathy — Neural Networks: Zero to Hero (GitHub repo) | https://github.com/karpathy/nn-zero-to-hero |
| *Deep Learning* — Goodfellow, Bengio, Courville | https://www.deeplearningbook.org |

**Proof:** implement backpropagation by hand, without a framework.

## Phase 3 — Computer Vision / Perception (6–8 weeks)

| Course / Resource | Link / Source |
|---|---|
| Stanford CS231n — course notes and assignments | https://cs231n.github.io |
| Stanford CS231n — syllabus | https://cs231n.stanford.edu |
| Stanford CS231n — lecture videos (YouTube, Spring 2017 edition) | https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv |
| OpenCV tutorials | https://docs.opencv.org |

**Proof:** train a CNN for real object detection on a dataset you sourced yourself.

## Phase 4 — Sequence Models & Transformers (3–4 weeks)

| Course / Resource | Link / Source |
|---|---|
| Stanford CS224n — course site | https://web.stanford.edu/class/cs224n |
| Stanford CS224n — lecture videos (YouTube) | https://www.youtube.com/playlist?list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z |
| Jay Alammar — The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer/ |

**Proof:** explain on a whiteboard what attention actually computes.

## Phase 5 — Reinforcement Learning (6–8 weeks)

| Course / Resource | Link / Source |
|---|---|
| Sutton & Barto — *Reinforcement Learning: An Introduction* (2nd ed.) | http://incompleteideas.net/book/the-book-2nd.html |
| David Silver's RL Course (UCL) — YouTube lectures (2015 edition) | https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9- |
| David Silver's RL Course (UCL) — slides | http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html |
| OpenAI Spinning Up in Deep RL | https://spinningup.openai.com |
| Gymnasium (CarRacing, LunarLander) | `pip install gymnasium` |

**Proof:** train an agent from scratch that solves a Gymnasium environment; justify PPO vs. DQN.

## Phase 6 — Robotics & Control Theory (6–8 weeks)

| Course / Resource | Link / Source |
|---|---|
| Underactuated Robotics (Russ Tedrake, MIT) | https://underactuated.csail.mit.edu (also on MIT OpenCourseWare) |
| *Modern Robotics* (Lynch & Park) | https://modernrobotics.northwestern.edu |
| ROS2 official tutorials | https://docs.ros.org |

**Proof:** understand PID vs. MPC and when each one breaks down.

## Phase 7 — Autonomous Driving Stack (8–12 weeks)

| Course / Resource | Link / Source |
|---|---|
| CARLA simulator | https://carla.org |
| Waymo Open Dataset | https://waymo.com/open |
| Bojarski et al., *End to End Learning for Self-Driving Cars* (2016, PilotNet) | https://arxiv.org/abs/1604.07316 |
| Autoware (open-source AV stack) | https://autoware.org |
| Baidu Apollo (open-source AV stack) | https://github.com/ApolloAuto/apollo |

**Proof:** train a model in CARLA that drives from camera input and explain every pipeline stage.

## Phase 8 — Production Skills (parallel with Phases 6–7, 4–6 weeks)

| Course / Resource | Link / Source |
|---|---|
| C++ — learncpp.com | https://www.learncpp.com |
| Linux basics — freeCodeCamp Linux crash course (article with embedded video) | https://www.freecodecamp.org/news/learn-the-basics-of-the-linux-operating-system/ |
| Docker official docs & tutorial | https://docs.docker.com |

**Proof:** run a trained Python model inside a basic ROS2 node.

## Phase 9 — Capstone Portfolio (8–12 weeks)

| Project | Resources Used |
|---|---|
| 1. Re-implement PilotNet and drive in CARLA | https://arxiv.org/abs/1604.07316 + https://carla.org |
| 2. RL agent for a driving decision (lane change, following distance) | https://github.com/Farama-Foundation/HighwayEnv (docs: https://highway-env.farama.org) or CARLA |
| 3. Perception pipeline: object detection + tracking | https://waymo.com/open |
| 4. One small contribution to Autoware or Apollo | https://autoware.org / https://github.com/ApolloAuto/apollo |

Put all four on GitHub with clear READMEs (what it does, what you learned, what you'd improve).

---

## Honest Notes

- Treat any "self-driving cars in a weekend" promise as a red flag.
- Phase 8 can run alongside Phases 6–7; Phases 5 (RL) and 6 (Robotics) can be swapped.
- Resources were live as of September 2026. Courses can move or get paywalled, so search by name if a link is dead.
- Some YouTube playlists are older editions of the course (CS231n is 2017, Silver's RL is 2015). The content is still the standard reference, but newer versions exist on the official course sites.
