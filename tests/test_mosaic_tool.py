"""
モザイクツールのCLIインターフェースのテスト
"""
import os
import pytest
from click.testing import CliRunner
import tempfile
from PIL import Image

# テスト対象のインポート
# テスト駆動開発では、まだ実装していないモジュールをインポートするため、一時的にエラーが発生します
from src.mosaic_tool import cli


class TestMosaicTool:
    """
    MosaicToolクラスのCLIインターフェースのテスト
    """
    
    def setup_method(self):
        """
        テスト前の準備
        """
        self.runner = CliRunner()
        # テスト用の入力画像を作成
        self.test_image = Image.new('RGB', (50, 50), color='blue')
    
    def test_cli_help(self):
        """
        ヘルプコマンドが正しく表示されるかテスト
        """
        result = self.runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert 'Usage:' in result.output
        assert '--strength' in result.output
        assert '--mode' in result.output
    
    def test_cli_invalid_input(self):
        """
        存在しない入力ファイルを指定した場合のエラーメッセージをテスト
        """
        result = self.runner.invoke(cli, ['non_existent_file.jpg', 'output.jpg'])
        assert result.exit_code != 0
        assert 'Error' in result.output or '存在しません' in result.output
    
    def test_cli_basic_mosaic(self):
        """
        基本的なモザイク処理が実行できるかテスト
        """
        # 一時ファイルに画像を保存
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as input_file:
            input_path = input_file.name
            self.test_image.save(input_path)
            
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as output_file:
            output_path = output_file.name
            
        try:
            # CLIコマンドを実行
            result = self.runner.invoke(cli, [
                input_path,
                output_path,
                '--strength', '5',
                '--mode', 'full'
            ])
            
            # コマンドが成功したことを確認
            assert result.exit_code == 0
            
            # 出力ファイルが生成されたことを確認
            assert os.path.exists(output_path)
            
            # 生成されたファイルが有効な画像であることを確認
            output_image = Image.open(output_path)
            assert output_image.size == (50, 50)
            
        finally:
            # テスト終了後に一時ファイルを削除
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_path):
                os.remove(output_path)
    
    def test_cli_face_mode(self):
        """
        顔検出モードでのモザイク処理が実行できるかテスト
        """
        # 一時ファイルに画像を保存
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as input_file:
            input_path = input_file.name
            self.test_image.save(input_path)
            
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as output_file:
            output_path = output_file.name
            
        try:
            # CLIコマンドを実行
            result = self.runner.invoke(cli, [
                input_path,
                output_path,
                '--strength', '5',
                '--mode', 'face'
            ])
            
            # コマンドが成功したことを確認
            assert result.exit_code == 0
            
            # 出力ファイルが生成されたことを確認
            assert os.path.exists(output_path)
            
            # 生成されたファイルが有効な画像であることを確認
            output_image = Image.open(output_path)
            assert output_image.size == (50, 50)
            
        finally:
            # テスト終了後に一時ファイルを削除
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_path):
                os.remove(output_path) 
