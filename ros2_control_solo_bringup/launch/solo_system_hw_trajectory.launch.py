from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    log_level = LaunchConfiguration('log_level')
    declare_log_level_argument = DeclareLaunchArgument(
        name='log_level',
        default_value='WARN',
        description='Log level')

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("ros2_description_solo"),
                    "urdf",
                    "solo12.urdf.xacro",
                ]
            ),
            " use_sim:=false",
            " use_fake_hardware:=false",
        ]
    )

    robot_description = {"robot_description": robot_description_content}

    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("ros2_control_solo_bringup"),
            "config",
            "solo_hw_trajectory_controller.yaml",
        ]
    )

    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers],
        output="both",
        arguments=['--ros-args', '--log-level', log_level],
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    spawn_joint_state_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    spawn_trajectory_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_trajectory_controller"],
        output="screen",
    )

    return LaunchDescription(
        [
            declare_log_level_argument,
            controller_manager_node,
            robot_state_publisher_node,
            spawn_joint_state_controller,
            spawn_trajectory_controller,
        ]
    )
