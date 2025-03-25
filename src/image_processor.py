"""
画像処理モジュール

画像の読み込み、保存、モザイク処理を行うクラスを提供します。
"""
from PIL import Image


class ImageProcessor:
    """
    画像処理を行うクラス
    
    画像の読み込み、モザイク処理、保存などの機能を提供します。
    """
    
    def load_image(self, image_path):
        """
        画像ファイルを読み込む
        
        Args:
            image_path: 画像ファイルのパス
            
        Returns:
            PIL.Image: 読み込んだ画像
            
        Raises:
            FileNotFoundError: 指定されたファイルが存在しない場合
            IOError: 画像の読み込みに失敗した場合
        """
        try:
            return Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"画像ファイル '{image_path}' が見つかりません")
        except IOError:
            raise IOError(f"画像ファイル '{image_path}' の読み込みに失敗しました")
    
    def apply_mosaic(self, image, strength):
        """
        画像にモザイク処理を適用する
        
        Args:
            image: PIL.Image オブジェクト
            strength: モザイクの強さ（1-10の整数、大きいほど強い）
            
        Returns:
            PIL.Image: モザイク処理された画像
            
        Raises:
            ValueError: strengthが1-10の範囲外の場合
        """
        if not 1 <= strength <= 10:
            raise ValueError("モザイクの強さは1から10の範囲で指定してください")
        
        # 元の画像サイズを保存
        width, height = image.size
        
        # モザイクの強さからブロックサイズを計算
        # 強度1: ブロックサイズ = 元の縦横の1/100
        # 強度10: ブロックサイズ = 元の縦横の1/10
        block_size = max(1, min(width, height) // (100 // strength))
        
        # サムネイルサイズを計算（元のアスペクト比を維持）
        thumbnail_width = max(1, width // block_size)
        thumbnail_height = max(1, height // block_size)
        
        # 縮小して荒くする
        small_image = image.resize((thumbnail_width, thumbnail_height), Image.NEAREST)
        
        # 元のサイズに戻す（ピクセルが大きくなる＝モザイク効果）
        result_image = small_image.resize((width, height), Image.NEAREST)
        
        return result_image
    
    def save_image(self, image, output_path):
        """
        画像を保存する
        
        Args:
            image: PIL.Image オブジェクト
            output_path: 保存先のファイルパス
            
        Raises:
            IOError: 画像の保存に失敗した場合
        """
        try:
            image.save(output_path)
        except IOError:
            raise IOError(f"画像の保存に失敗しました: {output_path}") 
