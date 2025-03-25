"""
顔検出モジュール

画像内の顔を検出し、顔領域にモザイク処理を適用するクラスを提供します。
"""
import cv2
import numpy as np
from PIL import Image


class FaceDetector:
    """
    画像内の顔を検出し、モザイク処理を適用するクラス
    """
    
    def __init__(self):
        """
        FaceDetectorの初期化
        
        OpenCVの顔検出器を読み込みます。
        """
        # OpenCVの顔検出用カスケード分類器を読み込む
        # 注: 実際の実装では、このパスがシステムに存在するか確認が必要
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def detect_faces(self, image):
        """
        画像内の顔を検出する
        
        Args:
            image: PIL.Image オブジェクト
            
        Returns:
            list: 顔の位置情報を含む辞書のリスト
                 各辞書は {'x': int, 'y': int, 'width': int, 'height': int} 形式
        """
        # PIL画像をOpenCV形式に変換
        cv_image = self._pil_to_cv(image)
        
        # グレースケールに変換
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        
        # 顔検出を実行
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # 検出結果を辞書のリストに変換
        face_list = []
        for (x, y, w, h) in faces:
            face_list.append({
                'x': x,
                'y': y,
                'width': w,
                'height': h
            })
        
        return face_list
    
    def apply_mosaic_to_faces(self, image, faces, strength):
        """
        検出された顔にモザイク処理を適用する
        
        Args:
            image: PIL.Image オブジェクト
            faces: 顔の位置情報を含む辞書のリスト
                  各辞書は {'x': int, 'y': int, 'width': int, 'height': int} 形式
            strength: モザイクの強さ (1-10)
            
        Returns:
            PIL.Image: 顔にモザイク処理が適用された画像
        """
        # 画像をコピー
        result_image = image.copy()
        
        # 顔がない場合は元の画像を返す
        if not faces:
            return result_image
        
        # PIL画像をOpenCV形式に変換
        cv_image = self._pil_to_cv(result_image)
        
        # 各顔にモザイク処理を適用
        for face in faces:
            x, y = face['x'], face['y']
            width, height = face['width'], face['height']
            
            # 顔の領域を切り出す
            face_region = cv_image[y:y+height, x:x+width]
            
            # モザイクの強さに応じてブロックサイズを決定
            block_size = max(1, min(width, height) // (30 // strength))
            
            # 縮小してからリサイズしてモザイク効果を作る
            small = cv2.resize(face_region, (width // block_size, height // block_size))
            mosaic_face = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)
            
            # モザイク処理した顔を元の画像に戻す
            cv_image[y:y+height, x:x+width] = mosaic_face
        
        # OpenCV画像をPIL形式に戻す
        return self._cv_to_pil(cv_image)
    
    def _pil_to_cv(self, pil_image):
        """
        PIL画像をOpenCV形式に変換
        
        Args:
            pil_image: PIL.Image オブジェクト
            
        Returns:
            numpy.ndarray: OpenCV形式の画像
        """
        # PIL画像をRGBに変換し、numpy配列に変換
        rgb_image = pil_image.convert('RGB')
        numpy_image = np.array(rgb_image)
        # RGBからBGRに変換（OpenCVはBGR形式を使用）
        return cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    
    def _cv_to_pil(self, cv_image):
        """
        OpenCV画像をPIL形式に変換
        
        Args:
            cv_image: numpy.ndarray (OpenCV形式の画像)
            
        Returns:
            PIL.Image: PIL形式の画像
        """
        # BGRからRGBに変換
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # numpy配列からPIL画像に変換
        return Image.fromarray(rgb_image) 
