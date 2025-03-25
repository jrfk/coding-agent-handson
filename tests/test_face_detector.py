"""
顔検出モジュールのテスト
"""
import os
import pytest
from PIL import Image
import tempfile

# テスト対象のインポート
# テスト駆動開発では、まだ実装していないモジュールをインポートするため、一時的にエラーが発生します
from src.face_detector import FaceDetector
from src.image_processor import ImageProcessor


class TestFaceDetector:
    """
    FaceDetectorクラスのテスト
    """
    
    def setup_method(self):
        """
        テスト前の準備
        """
        self.detector = FaceDetector()
        self.processor = ImageProcessor()
        
        # 一時的なテスト画像を作成（100x100のRGB画像）
        # 実際のテストでは顔の画像が必要ですが、ここではダミー画像を使用
        self.test_image = Image.new('RGB', (100, 100), color='white')
        
    def test_detect_faces(self):
        """
        顔検出のテスト
        注: このテストはダミー画像を使用しているため、実際には顔が検出されない
        実装時は実際の顔画像を用いたテストに置き換える必要がある
        """
        faces = self.detector.detect_faces(self.test_image)
        
        # ダミー画像では顔は検出されないはずなので、空のリストが返るはず
        assert faces == []
        
        # 注: 実際の顔画像を使った場合のテストは以下のようになる
        # faces = self.detector.detect_faces(real_face_image)
        # assert len(faces) > 0
        # for face in faces:
        #     assert 'x' in face
        #     assert 'y' in face
        #     assert 'width' in face
        #     assert 'height' in face
        
    def test_apply_mosaic_to_faces(self):
        """
        顔領域へのモザイク適用テスト
        """
        # ダミーの顔領域情報
        dummy_faces = [
            {'x': 10, 'y': 10, 'width': 30, 'height': 30}
        ]
        
        # モザイク適用テスト
        mosaic_image = self.detector.apply_mosaic_to_faces(
            self.test_image, dummy_faces, 5
        )
        
        # 結果の検証
        assert mosaic_image is not None
        assert mosaic_image.size == (100, 100)
        
        # 注: 実際の実装では、モザイクが適用された部分のピクセル値が
        # 元の画像と異なることを検証する必要がある 
