import os
import subprocess
import xml.etree.ElementTree as ET

import cv2



def update_xml_file(video_folder, video_filename):
    # XML 파일 수정
    targetXML = '/home/root1/anaconda3/envs/falldetection_ai/lib/python3.7/site-packages/openpifpaf/config/config.xml'
    tree = ET.parse(targetXML)
    root = tree.getroot()

    for rstpurl in root.iter('RTSPURL'):
        rstpurl.text = os.path.join(video_folder, video_filename)

    tree.write(targetXML, encoding='UTF-8')

def run_openpifpaf(video_folder, video_filename):
    # Openpifpaf 실행
    subprocess.run('cd /home/root1/anaconda3/envs/falldetection_ai/lib/python3.7/site-packages/openpifpaf/', shell=True)
    subprocess.run('python3 -m openpifpaf.video --show --video-fps=30', shell=True)

# 동영상 파일 경로
video_folder = '/home/root1/Desktop/videos/'

# 최근에 생성된 동영상 파일 가져오기
videos_name = '/home/root1/Desktop/videos_Preprocessor/videos.mp4'


# XML 파일 수정
update_xml_file(video_folder, videos_name)
#update_xml_file(video_folder, f'video{file_count + 1}.mp4')

# Openpifpaf 실행
run_openpifpaf(video_folder, videos_name)
#run_openpifpaf(video_folder, f'video{file_count + 1}.mp4')
