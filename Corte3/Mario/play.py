import torch
import time
from pathlib import Path
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym.wrappers import FrameStack, GrayScaleObservation, TransformObservation
from core import Mario, SkipFrame, ResizeObservation

env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
env = JoypadSpace(env, [['right'], ['right', 'A']])
env = SkipFrame(env, skip=4)
env = GrayScaleObservation(env, keep_dim=False)
env = ResizeObservation(env, shape=84)
env = TransformObservation(env, f=lambda x: x / 255.)
env = FrameStack(env, num_stack=4)

save_dir = Path('checkpoints') 
checkpoint = torch.load(str(save_dir / 'mario_net_3.chkpt'))

mario = Mario(state_dim=(4, 84, 84), action_dim=env.action_space.n, save_dir=save_dir)

mario.net.load_state_dict(checkpoint['model'])
mario.exploration_rate = checkpoint['exploration_rate']

mario.net.eval()

state = env.reset()
done = False

while not done:
    env.render()
    time.sleep(0.03)  
    action = mario.act(state)
    next_state, reward, done, info = env.step(action)
    state = next_state

    if done or info['flag_get']:
        break

env.close()