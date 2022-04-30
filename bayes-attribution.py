# coding: utf-8

# Setup the sample dataset
from alps.bayes_net import dataset, mock_dataset
bayes_samples = mock_dataset()

# Setup the attribution player
from alps.bayes_net import BayesNetPlayer
player = BayesNetPlayer(
	name='bayes_job',
	operation=BayesNetPlayer.Operation.ATTRIBUTION,
	sample_dataset=bayes_samples)

# Set the compute resource
from alps.framework.engine import KubemakerEngine
from alps.framework.engine import ResourceConf
player.set_trial_engine(KubemakerEngine(
	worker=ResourceConf(core=4, memory=8192, num=8)))

# Set parallel used in the attribution process
player.set_explore_size(4)

# Set valid probability threshold
player.set_threshold(0.84)

# Set attribution target and its value
player.set_target_name("x9").set_target_value(1)

# Start attribution
future = player.play()

# Waiting for the attribution result and output
attri_result = future.result()
print(attri_result)
