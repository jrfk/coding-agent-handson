"""
画像処理モジュールのテスト
"""
import os
import pytest
from PIL import Image
import tempfile

# テスト対象のインポート
# テスト駆動開発では、まだ実装していないモジュールをインポートするため、一時的にエラーが発生します
from src.image_processor import ImageProcessor


class TestImageProcessor:
    """
    ImageProcessorクラスのテスト
    """
    
    def setup_method(self):
        """
        テスト前の準備
        """
        self.processor = ImageProcessor()
        # 一時的なテスト画像を作成（10x10のRGB画像）
        self.test_image = Image.new('RGB', (10, 10), color='red')
        
    def test_load_image(self):
        """
        画像読み込みのテスト
        """
        # 一時ファイルに画像を保存
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_path = temp_file.name
            self.test_image.save(temp_path)
        
        try:
            # 読み込みテスト
            loaded_image = self.processor.load_image(temp_path)
            assert loaded_image is not None
            assert loaded_image.size == (10, 10)
            assert loaded_image.mode == 'RGB'
        finally:
            # テスト終了後に一時ファイルを削除
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    def test_apply_mosaic(self):
        """
        モザイク処理のテスト
        """
        # 強度1（最弱）でモザイク処理
        mosaic_image_weak = self.processor.apply_mosaic(self.test_image, 1)
        assert mosaic_image_weak is not None
        assert mosaic_image_weak.size == (10, 10)
        
        # 強度10（最強）でモザイク処理
        mosaic_image_strong = self.processor.apply_mosaic(self.test_image, 10)
        assert mosaic_image_strong is not None
        assert mosaic_image_strong.size == (10, 10)
        
        # 弱いモザイクと強いモザイクは異なる結果になるはず
        # ただし、単色画像ではテストが難しいため、実際の実装では詳細なテストが必要
        
    def test_save_image(self):
        """
        画像保存のテスト
        """
        # 一時ファイルに画像を保存
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_path = temp_file.name
            
        try:
            # 保存テスト
            self.processor.save_image(self.test_image, temp_path)
            
            # 保存されたファイルが存在するか確認
            assert os.path.exists(temp_path)
            
            # 保存された画像が正しく読み込めるか確認
            saved_image = Image.open(temp_path)
            assert saved_image.size == (10, 10)
            assert saved_image.mode == 'RGB'
        finally:
            # テスト終了後に一時ファイルを削除
            if os.path.exists(temp_path):
                os.remove(temp_path) 
