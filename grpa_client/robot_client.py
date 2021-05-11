import asyncio, robot
from socketio import AsyncClient
from os import getcwd
from os.path import join

loop = asyncio.get_event_loop()
sio = AsyncClient()
log_dir = join(getcwd(), 'log')
template_dir = join(getcwd(), 'process/excel')


@sio.event
async def connect():
    print("just connected")


@sio.event
async def disconnect():
    print("disconnected")


@sio.event
async def start_robot(data):
    print('start_robot event called')
    with open(join(log_dir, 'robot.log'), 'w') as log_file:
        template_path = join(template_dir, data['template_name'])
        print('Robot {0} will be executed.'.format(template_path))
        robot.run(template_path, stdout=log_file, outputdir=log_dir)
        print('Execution done')


async def my_main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    loop.run_until_complete(my_main())
