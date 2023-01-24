# coding: utf-8

# These are the sample codes to perform the attribution using our bayesian network system.
# Because the system is used internally for now and necessary modules couldn't be imported,
# e.g. alps, the codes only explain Python interface of our system. In the conference we will
# prepare the docker image. We also show GUI in the link
# https://github.com/cuauty/demo-2022/blob/main/distri-bayes-demo.mp4?raw=true

# Setup the sample dataset
from alps.bayes_net import dataset, mock_dataset
bayes_samples = mock_dataset()

# Setup the attribution player
from alps.bayes_net import BayesNetPlayer
player = BayesNetPlayer(
        name='bayes_job',
        operation=BayesNetPlayer.Operation.SEARCH,
        sample_dataset=bayes_samples)

# Set parallel used in the attribution process
player.set_explore_size(4)

# Set attribution target and its value
player.set_target_name("x9").set_target_value(1)

# Start attribution
future = player.play()

# Waiting for the attribution result and output
attri_result = future.result()
print(attri_result)
