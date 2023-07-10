#!"C:\xampp\perl\bin\perl.exe"

use CGI;
$cgi = CGI->new();

# データの保存先のファイル
my $filepath = "./data/forum.txt";
my $data;

# カウンタ
my $counter_file = './data/counter.txt';  # カウンタのファイルパスを適宜変更してください
my $counter = read_counter_from_file($counter_file) || 0;
$counter++;
write_counter_to_file($counter_file, $counter);

# カウンタの値をファイルに保存するサブルーチン
sub write_data{
    my ($name, $message, $num) = @_;
    open(my $fh, '>>:encoding(utf8)', $filepath);
    print $fh "$num :$name<br>$message<br>\n";
    close($fh);
}

# データをファイルから読み込むサブルーチン
sub read_print_data{
    my ($file) = @_;
    if (-e $file) {
        open(my $fh, '<', $filepath) or die "Failed to open forum file: $!";
        my @lines = <$fh>;
        
        # 読み込んだ行を表示する
        foreach my $line (@lines) {
            $cgi->print("$line<br>");
        }

        close($fh);
        return @data;
    }
    return undef;
}

# カウンタの値をファイルから読み込むサブルーチン
sub read_counter_from_file {
    my ($file) = @_;
    if (-e $file) {
        open(my $fh, '<', $file) or die "Failed to open counter file: $!";
        my $counter = <$fh>;
        close($fh);
        chomp($counter);
        return $counter;
    }
    return undef;
}

# カウンタの値をファイルに保存するサブルーチン
sub write_counter_to_file {
    my ($file, $counter) = @_;
    open(my $fh, '>', $file) or die "Failed to open counter file: $!";
    print $fh $counter;
    close($fh);
}


# ------------------HTML------------------- 
print $cgi->header('text/html');


# レスポンスのボディを出力
print "<html>\n";
print "<head><title>Forum</title></head>\n";
print "<body>\n";


# フォームデータの取得と表示
if ($cgi->param('submit')) {
    # フォームからのデータの取得
    my $username = $cgi->param('username');
    my $message = $cgi->param('message');

    # データの出力はここから
    print "<h1>View Data</h1>";

    # ファイルにデータを書き込み
    if($username eq '' || $message eq ''){
        print "<h5>Username or message is empty!</h5>\n";
    }
    else {
        $counter++;
        write_data("$username", "$message" , "$counter");
    }

    # ファイルからデータを読み込み
    my @data = read_print_data($filepath) || "no data to display.";
    print "<p>$data</p>\n";

}

print $cgi->start_form;  # フォームの開始

print "<h1>Forum site</h1>\n";
print "<label for='username'>name:</label>\n";
print $cgi->textfield('username');  
print "<br>\n";
print $cgi->textarea(-name => 'message', -rows => 6, -cols => 40);
print "<br>\n";

print $cgi->submit('submit', 'Submit');  # 送信ボタン

print $cgi->end_form;  # フォームの終了

print "</body>\n";
print "</html>\n";