"""
モザイク処理ツールのCLIインターフェース

画像にモザイク処理を適用するためのコマンドラインインターフェースを提供します。
"""
import os
import sys
import click
from .image_processor import ImageProcessor
from .face_detector import FaceDetector


@click.command()
@click.argument('input_image', type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument('output_image', type=click.Path(dir_okay=False, writable=True))
@click.option('--strength', type=click.IntRange(1, 10), default=5,
              help='モザイクの強さ（1-10、大きいほど強い）')
@click.option('--mode', type=click.Choice(['full', 'face']), default='full',
              help='処理モード（full: 画像全体、face: 顔のみ）')
def cli(input_image, output_image, strength, mode):
    """
    画像にモザイク処理を適用するコマンドラインツール
    
    INPUT_IMAGE: 入力画像ファイルのパス
    OUTPUT_IMAGE: 出力画像ファイルのパス
    """
    try:
        processor = ImageProcessor()
        detector = FaceDetector()
        
        # 画像を読み込む
        click.echo(f"画像を読み込んでいます: {input_image}")
        image = processor.load_image(input_image)
        
        # モード選択
        if mode == 'full':
            # 画像全体にモザイク処理を適用
            click.echo(f"画像全体にモザイク処理を適用しています（強さ: {strength}）")
            processed_image = processor.apply_mosaic(image, strength)
        else:
            # 顔検出を実行
            click.echo("顔検出を実行しています...")
            faces = detector.detect_faces(image)
            
            if faces:
                click.echo(f"{len(faces)}個の顔を検出しました")
                click.echo(f"顔領域にモザイク処理を適用しています（強さ: {strength}）")
                processed_image = detector.apply_mosaic_to_faces(image, faces, strength)
            else:
                click.echo("顔が検出されませんでした。元の画像を保存します。")
                processed_image = image
        
        # 処理結果を保存
        click.echo(f"処理結果を保存しています: {output_image}")
        processor.save_image(processed_image, output_image)
        
        click.echo("処理が完了しました")
        return 0
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        return 1


if __name__ == '__main__':
    sys.exit(cli()) 
