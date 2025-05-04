#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

class JointStateReader(object):
    def __init__(self):
        self._joint_states = {}
        rospy.Subscriber('/joint_states', JointState, self._callback)

    def _callback(self, msg):
        for name, position in zip(msg.name, msg.position):
            self._joint_states[name] = position

    def get_joint(self, name):
        return self._joint_states.get(name)

    def get_joints(self, names):
        return [self._joint_states.get(n) for n in names]
