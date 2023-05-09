from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    config_obstacle = LaunchConfiguration('obstacle', default='0.3')
    config_degrees = LaunchConfiguration('degrees', default='90')
    config_final_approach = LaunchConfiguration('final_approach', default='False')

    declare_obstacle = DeclareLaunchArgument(
        'obstacle',
        default_value=config_obstacle,
        description='Obstacle distance parameter'
    )
    
    declare_degrees = DeclareLaunchArgument(
        'degrees',
        default_value=config_degrees,
        description='Degrees of rotation parameter'
    )
    
    declare_final_approach = DeclareLaunchArgument(
        'final_approach',
        default_value=config_final_approach,
        description='Final approach parameter'
    )

    pre_approach_v2_node = Node(
        package='attach_shelf',
        executable='pre_approach_v2',
        name='pre_approach_v2',
        parameters=[{
            'obstacle': config_obstacle,
            'degrees': config_degrees,
            'final_approach': config_final_approach
        }]
    )

    approach_service_server_node = Node(
        package='attach_shelf',
        executable='approach_service_server',
        name='approach_service_server'
    )

    return LaunchDescription([
        declare_obstacle,
        declare_degrees,
        declare_final_approach,
        pre_approach_v2_node,
        approach_service_server_node
    ])
