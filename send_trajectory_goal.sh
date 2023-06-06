ros2 action send_goal /joint_trajectory_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory -f "{
  trajectory: {
    joint_names: [FL_HAA, FL_HFE, FL_KFE, FR_HAA, FR_HFE, FR_KFE, HL_HAA, HL_HFE, HL_KFE, HR_HAA, HR_HFE, HR_KFE],
    points: [
      {
        positions: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        time_from_start: { sec: 1 }
      }
    ]
  },
  goal_tolerance: [
    { name: FL_HAA, position: 0.1 },
    { name: FL_HFE, position: 0.1 },
    { name: FL_KFE, position: 0.1 },
    { name: FR_HAA, position: 0.1 },
    { name: FR_HFE, position: 0.1 },
    { name: FR_KFE, position: 0.1 },
    { name: HL_HAA, position: 0.1 },
    { name: HL_HFE, position: 0.1 },
    { name: HL_KFE, position: 0.1 },
    { name: HR_HAA, position: 0.1 },
    { name: HR_HFE, position: 0.1 },
    { name: HR_KFE, position: 0.1 }
  ]
}"