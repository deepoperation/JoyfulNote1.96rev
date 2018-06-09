#!/usr/local/bin/perl

#��������������������������������������������������������������������
#��  JOYFUL NOTE v1.96 (2006/01/18)
#��  Copyright (c) KentWeb
#��  webmaster@kent-web.com
#��  http://www.kent-web.com/
#��  
#��  Improved by deepoperation(2018)(c)
#��  https://github.com/deepoperation/JoyfulNote1.96rev
#��������������������������������������������������������������������
$ver = 'JoyfulNote v1.96';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#�� 3. ���̃X�N���v�g�́Amethod=POST ��p�ł��B	
#�� 4. �����̃A�C�R���ŁA�ȉ��̃t�@�C���̒��쌠�҂͈ȉ��̂Ƃ���ł��B
#��    home.gif : mayuRin����
#��    clip.gif : �������ƃA�C�R���̕�������
#��������������������������������������������������������������������
#
# �y�t�@�C���\����z
#
#  public_html (�z�[���f�B���N�g��)
#      |
#      +-- joyful / joyful.cgi [705]
#            |      joyful.log [606]
#            |      count.dat  [606]
#            |      jcode.pl   [604]
#            |      cgi-lib.pl [604]
#            |      pastno.dat [606]
#            |
#            +-- img  [707] / home.gif, bear.gif, ...
#            |
#            +-- lock [707] /
#            |
#            +-- past [707] / 1.dat [606] ...

#-------------------------------------------------
#  �ݒ荀��
#-------------------------------------------------

# ���C�u�����捞
require './jcode.pl';
require './cgi-lib.pl';

# �^�C�g����
$title = "";

# �^�C�g���̕����F
$t_color = "#804040";

# �^�C�g���̕����T�C�Y
$t_size = '26px';

# �{���̕����t�H���g
$face = '"�l�r �S�V�b�N", "MS UI Gothic", Osaka-mono, Osaka';

# �{���̕����T�C�Y
$b_size = '16px';

# �ǎ����w�肷��ꍇ�ihttp://����w��j
$bg = "";

# �w�i�F���w��
$bc = "#FEF5DA";

# �����F���w��
$tx = "#000000";

# �����N�F���w��
$lk = "#0000FF";	# ���K��
$vl = "#800080";	# �K���
$al = "#FF0000";	# �K�⒆

# �߂���URL (index.html�Ȃ�)
$homepage = "";

# �ő�L���� (�e�L��+���X�L�����܂߂����j
$max = 800;

# �ő�ԐM��
$maxres = 30;

# �Ǘ��җp�}�X�^�p�X���[�h (�p�����łW�����ȓ�)
$pass = '';

# �ԐM�����Ɛe�L�����g�b�v�ֈړ� (0=no 1=yes)
$topsort = 1;

# �ԐM�ɂ��Y�t�@�\�������� (0=no 1=yes)
$res_clip = 1;

# �摜�ƋL���̈ʒu
#  1 : �摜�����B�L���͉E�����荞��
#  2 : �摜�����B�L���͉摜�̏�ɕ\���B
$imgpoint = 2;

# �^�C�g����GIF�摜���g�p���鎞 (http://����L�q)
$t_img = "";
$t_w = 180;	# GIF�摜�̕� (�s�N�Z��)
$t_h = 40;	#    �V    ���� (�s�N�Z��)

# �t�@�C�����b�N�`��
# �� 0=no 1=symlink�֐� 2=mkdir�֐�
$lockkey = 2;

# ���b�N�t�@�C����
$lockfile = './lock/joyful.lock';

# �~�j�J�E���^�̐ݒu
# �� 0=no 1=�e�L�X�g 2=GIF�摜
$counter = 1;

# �~�j�J�E���^�̌���
$mini_fig = 7;

# �e�L�X�g�̂Ƃ��F�~�j�J�E���^�̐F
$cnt_color = "#BB0000";

# GIF�J�E���^�̂Ƃ��F�摜�܂ł̃f�B���N�g��
# �� �Ō�͕K�� / �ŕ���
$gif_path = "./img/";
$mini_w = 8;		# �摜�̉��T�C�Y
$mini_h = 12;		# �摜�̏c�T�C�Y

# �J�E���^�t�@�C��
$cntfile = './count.dat';

# �X�N���v�g��URL
$script = './joyful.cgi';

# ���O�t�@�C�����w��
# �� �t���p�X�Ŏw�肷��ꍇ�� / ����L�q
$logfile = './joyfullog.cgi';

# �A�b�v���[�h�f�B���N�g��
# �� �p�X�̍Ō�� / �ŏI��邱��
# �� �t���p�X���� / ����L�q����
$imgdir = './img/';

# �A�b�v���[�h�f�B���N�g���̂t�q�k�p�X
# �� �p�X�̍Ō�� / �ŏI��邱��
$imgurl = "http://www.xxx.xxx/~xxx/img/";
$imgurl = "./img/";

# �Y�t�t�@�C���̃A�b�v���[�h�Ɏ��s�����Ƃ�
#   0 : �Y�t�t�@�C���͖������A�L���͎󗝂���
#   1 : �G���[�\�����ď����𒆒f����
$clip_err = 1;

# �L�� [�^�C�g��] ���̒��� (�S�p�������Z)
$sub_len = 30;

# ���[���A�h���X�̓��͕K�{ (0=no 1=yes)
$in_email = 0;

# �L���� [�^�C�g��] ���̐F
$sub_color = "#880000";

# �L���\�����̉��n�̐F
$tbl_color = "#FFFFFF";

# ����IP�A�h���X����̘A�����e���ԁi�b���j
# �� �A�����e�Ȃǂ̍r�炵�΍�
# �� �l�� 0 �ɂ���Ƃ��̋@�\�͖����ɂȂ�܂�
$wait = 120;

# �P�y�[�W������̋L���\���� (�e�L��)
$p_log = 20;

# ���e������ƃ��[���ʒm���� (sendmail�K�{)
#  0 : �ʒm���Ȃ�
#  1 : �ʒm���邪�A�����̓��e�L���̓��[�����Ȃ��B
#  2 : �ʒm����B�����̓��e�L�����ʒm����B
$mailing = 0;

# ���[���A�h���X(���[���ʒm���鎞)
$mailto = 'xxx@xxx.xxx';

# sendmail�p�X�i���[���ʒm���鎞�j
$sendmail = '/usr/lib/sendmail';

# ���T�C�g���瓊�e�r�����Ɏw�� (http://���珑��)
$base_url = "";

# �����F�̐ݒ�i���p�X�y�[�X�ŋ�؂�j
$colors = '#800000 #DF0000 #008040 #0000FF #C100C1 #FF80C0 #FF8040 #000080';

# URL�̎��������N (0=no 1=yes)
$autolink = 1;

# ����n���h��
$handles = '';

# �^�O�L���}���I�v�V����
# �� <!-- �㕔 --> <!-- ���� --> �̑���Ɂu�L���^�O�v��}������B
# �� �L���^�O�ȊO�ɁAMIDI�^�O �� LimeCounter���̃^�O�ɂ��g�p�\�ł��B
$banner1 = '<!-- �㕔 -->';	# �f���㕔�ɑ}��
$banner2 = '<!-- ���� -->';	# �f�������ɑ}��

# �z�X�g�擾���@
# 0 : gethostbyaddr�֐����g��Ȃ�
# 1 : gethostbyaddr�֐����g��
$gethostbyaddr = 0;

# �A�N�Z�X�����i���p�X�y�[�X�ŋ�؂�A�A�X�^���X�N�j
#  �� ���ۃz�X�g�����L�q�i�����v�j�y��z*.anonymizer.com
$deny_host = '*.example.com *.hidehost.net *.su *.ru *.dynamic.163data.com.cn *.cust.vpntunnel.se *.kyivstar.net';
#  �� ����IP�A�h���X���L�q�i�O����v�j�y��z210.12.345.*
$deny_addr = '116.1.*';

#  �� ���ۃz�X�g�����L�q�i�����v�j�y��z*.anonymizer.com
$deny_host2 = '';
#  �� ����IP�A�h���X���L�q�i�O����v�j�y��z210.12.345.*
$deny_addr2 = '';

#  �� ���ۃz�X�g�����L�q�i�����v�j�y��z*.anonymizer.com
$deny_host3 = '';
#  �� ����IP�A�h���X���L�q�i�O����v�j�y��z210.12.345.*
$deny_addr3 = '';

$allow_addr = '';
$allow_host = '';

# �A�b�v���[�h��������t�@�C���`��
#  0:no  1:yes
$gif   = 1;	# GIF�t�@�C��
$jpeg  = 1;	# JPEG�t�@�C��
$png   = 1;	# PNG�t�@�C��
$text  = 1;	# TEXT�t�@�C��
$lha   = 1;	# LHA�t�@�C��
$zip   = 1;	# ZIP�t�@�C��
$pdf   = 1;	# PDF�t�@�C��
$midi  = 1;	# MIDI�t�@�C��
$word  = 1;	# WORD�t�@�C��
$excel = 1;	# EXCEL�t�@�C��
$ppt   = 1;	# POWERPOINT�t�@�C��
$ram   = 0;	# RAM�t�@�C��
$rm    = 0;	# RM�t�@�C��
$mpeg  = 0;	# MPEG�t�@�C��
$mp3   = 0;	# MP3�t�@�C��
$kif   = 1;
$ki2   = 1;
$csa   = 1;
$bod   = 1;
$gbd   = 1;
$gam   = 1;

# ���e�󗝍ő�T�C�Y (bytes)
# �� �� : 102400 = 100KB
$cgi_lib'maxdata = 4096000;

# �摜�t�@�C���̍ő�\���̑傫���i�P�ʁF�s�N�Z���j
# �� ����𒴂���摜�͏k���\�����܂�
$MaxW = 300;	# ����
$MaxH = 300;	# �c��

# �ƃA�C�R���̎g�p (0=no 1=yes)
$home_icon = 1;

# �A�C�R���摜�t�@�C���� (�t�@�C�����̂�)
$IconHome = "home.gif";  # �z�[��
$IconClip = "clip.gif";  # �N���b�v
$IconSoon = "soon.gif";  # COMINIG SOON

# �摜�Ǘ��҃`�F�b�N�@�\ (0=no 1=yes)
# �� �A�b�v���[�h�u�摜�v�͊Ǘ��҂��`�F�b�N���Ȃ��ƕ\������Ȃ��@�\�ł�
# �� �`�F�b�N�����܂Łu�摜�v�́uCOMMING SOON�v�̃A�C�R�����\������܂�
$ImageCheck = 0;

# ���e��̏���
#  �� �f�����g��URL���L�q���Ă����ƁA���e�ナ���[�h���܂�
#  �� �u���E�U���ēǂݍ��݂��Ă���d���e����Ȃ��[�u�B
#  �� Location�w�b�_�̎g�p�\�ȃT�[�o�̂�
$location = '';

# �֎~���[�h
#  �� �R���}�ŋ�؂��ĕ����w�肷��i��j$deny_word = '�A�_���g,�o�,�J�b�v��';
$deny_word = 'http://';

#---(�ȉ��́u�ߋ����O�v�@�\���g�p����ꍇ�̐ݒ�ł�)---#
#
# �ߋ����O���� (0=no 1=yes)
$pastkey = 1;

# �ߋ����O�pNO�t�@�C��
$nofile  = './pastno.dat';

# �ߋ����O�̃f�B���N�g��
# �� �t���p�X�Ȃ� / ����L�q�ihttp://����ł͂Ȃ��j
# �� �Ō�͕K�� / �ŕ���
$pastdir = './past/';

# �ߋ����O�P�t�@�C���̍s��
# �� ���̍s���𒴂���Ǝ��y�[�W�������������܂�
$log_line = 2000;

#-------------------------------------------------
#  �ݒ芮��
#-------------------------------------------------

# ���C������
&decode;
&get_time;

# IP&�z�X�g�擾
$host = $ENV{'REMOTE_HOST'};
$addr = $ENV{'REMOTE_ADDR'};

if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
	$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
}
$http_accept = $ENV{'HTTP_ACCEPT'};	# �N���C�A���g���󂯕t���邱�Ƃ��ł���MIME�^�C�v�̃��X�g
$user_agent	= $ENV{'HTTP_USER_AGENT'};	# �N���C�A���g�����N�G�X�g�𔭍s����Ƃ��Ɏg�p����u���E�U��
$http_referer = $ENV{'HTTP_REFERER'};	# �Ăяo������URL�B
$http_via = $ENV{'HTTP_VIA'};
$forwerded_for = $ENV{'HTTP_X_FORWARDED_FOR'};
$forwarded_host = "";
$forwarded = $ENV{'HTTP_FORWARDED'};

if($user_agent =~ "komaviewer")
{
	$autolink = 0;
}

# ���Ԃ̎擾
$security = sprintf("%04d%02d%02d",$year+1900,$mon+1,$mday);
$proxy_file = sprintf("%04d%02d",$year+1900,$mon+1) . "proxy" . ".cgi";
$security = $security . ".cgi";

#open(DATA,">> $security") || &error("Open Error: $security");
#flock(DATA, 2);
#print DATA "$date\t$script\t$retstring\t$host\t$addr\t$http_accept\t$user_agent\t$http_referer\t$http_via\t$forwerded_for\t$forwarded_host\t$forwarded\t$mode\n";
#close(DATA);

# �J�E���^����
&axscheck;

if ($mode eq "howto") { &howto; }
elsif ($mode eq "find") { &find; }
elsif ($mode eq "usr_del"){ &usr_del; }
elsif ($mode eq "usr_edt")
{
#	&writecheck;
	&usr_edt;
}
elsif ($mode eq "regist")
{
	&writecheck;
	&regist;
}
elsif ($mode eq "res"){ &res_form; }
elsif ($mode eq "thview"){ &thview; }
elsif ($mode eq "admin") { &admin; }
elsif ($mode eq "past") { &past; }
elsif ($mode eq "check") { &check; }
elsif ($mode eq "list") { &list; }
&html_log;

#-------------------------------------------------
#  �v���L�V�����Ȃ�
#-------------------------------------------------
sub writecheck {
	$retstring = "OK";
	# ����n���h���`�F�b�N
	foreach ( split(/\s+/, $handles) )
	{
		if ($in{'name'} =~ /$_$/i) { return; }
	}
	foreach ( split(/\s+/, $allow_addr) )
	{
		s/\./\\\./g;
		s/\*/\.\*/g;
		if ($addr =~ /^$_/i)
		{
			return;
		}
	}
	foreach ( split(/\s+/, $allow_host) )
	{
		s/\./\\\./g;
		s/\*/\.\*/g;
			
		if ($host =~ /$_$/i) { return; }
	}
	# IP�`�F�b�N
	local($flg);
	foreach ( split(/\s+/, $deny_addr2) )
	{
		s/\./\\\./g;
		s/\*/\.\*/g;
		if ($addr =~ /^$_/i) { $flg = 1; last; }
	}
	if ($flg)
	{
		&error("���e��������Ă��܂���");
		# �z�X�g�`�F�b�N
	}
	elsif($host)
	{
		foreach ( split(/\s+/, $deny_host2) )
		{
			s/\./\\\./g;
			s/\*/\.\*/g;
			
			if ($host =~ /$_$/i) { $flg = 1; last; }
		}
		if ($flg)
		{
			&error("���e��������Ă��܂���");
		}
	}
	foreach ( split(/\s+/, $deny_addr3) )
	{
		s/\./\\\./g;
		s/\*/\.\*/g;
		if ($addr =~ /^$_/i) { $flg = 1; last; }
	}
	if ($flg)
	{
		if(index($in{'sub'},"�����[", ) < 0 || !$in{'reno'}) {
			&error("���e��������Ă��܂���");
		}
		# �z�X�g�`�F�b�N
	}
	elsif($host)
	{
		foreach ( split(/\s+/, $deny_host3) )
		{
			s/\./\\\./g;
			s/\*/\.\*/g;
			
			if ($host =~ /$_$/i) { $flg = 1; last; }
		}
		if ($flg)
		{
			if(index($in{'sub'},"�����[", ) < 0 || !$in{'reno'}) {
				&error("���e��������Ă��܂���");
			}
		}
	}
	my @DNSBL_list = ('all.rbl.jp','bsb.spamlookup.net','http.dnsbl.sorbs.net');
	my $RADDR = $ENV{'REMOTE_ADDR'}; 
	
	foreach my $DNSBL_host (@DNSBL_list){ 
		$RADDR =~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/; 
		my $query_addr = "$4.$3.$2.$1.$DNSBL_host"; 
		my $result = join('.', unpack('C*', gethostbyname($query_addr))); 

		if ($result =~ /^127\.0\.0\./){ 
			# �X�p������Ɉ��������������̏��� ���K���ɕύX 
			$retstring = 'NG:' . $DNSBL_host;
		} 
	} 
	if ($retstring eq "OK" and  $host eq $addr){ 
		# �X�p������Ɉ��������������̏��� ���K���ɕύX 
		$retstring = 'NG:' . "NoName";
	} 
	if($retstring ne "OK") {
			&error("���J�v���L�V����̓��e�͋�����Ă��܂���<BR>");
	}
}

#-------------------------------------------------
#  �A�N�Z�X����
#-------------------------------------------------
sub axscheck {	
	local($flg);
	foreach ( split(/\s+/, $deny_addr) )
	{
		s/\./\\\./g;
		s/\*/\.\*/g;
		if ($addr =~ /^$_/i) { $flg = 1; last; }
	}
	if ($flg)
	{
		&error("�A�N�Z�X��������Ă��܂���");

		# �z�X�g�`�F�b�N
	}
	elsif($host)
	{
		foreach ( split(/\s+/, $deny_host) )
		{
			s/\./\\\./g;
			s/\*/\.\*/g;
			
			if ($host =~ /$_$/i) { $flg = 1; last; }
		}
		if ($flg)
		{
			&error("�A�N�Z�X��������Ă��܂���");
		}
	}
#	if ($ENV{'HTTP_FROM'}||$ENV{'HTTP_VIA'}||$ENV{'HTTP_X_FORWARDED_FOR'})
#	{
#		&error("proxy�o�R�ł͏������݂ł��܂���");
#	}
	if($host eq "") { $host = $addr; }
}

#-------------------------------------------------
#  �L���\����
#-------------------------------------------------
sub html_log {
	local($ipt,$wh,$i,$flag,$rescount);
	# �w�b�_���o��
	&header;

	# �J�E���^����
	if ($counter) { &counter; }

	# �^�C�g����
	print "<div align='center'>\n";
	if ($banner1 ne "<!-- �㕔 -->") { print "$banner1<p>\n"; }
	if ($t_img eq '') {
		print "<b style=\"font-size:$t_size;color:$t_color;\">$title</b>\n";
	} else {
		print "<img src=\"$t_img\" width=\"$t_w\" height=\"$t_h\" alt=\"$title\">\n";
	}

	# ���j���[��
	print "<hr width=\"90%\">\n";
	print "[<a href=\"$homepage\" target=\"_top\">�g�b�v�ɖ߂�</a>]\n";
	print "[<a href=\"$script?mode=howto\">���ӎ���</a>]\n";
	print "[<a href=\"$script?mode=find\">���[�h����</a>]\n";
	print "[<a href=\"$script?mode=list\">�X���b�h���X�g</a>]\n";
	print "[<a href=\"$script?mode=past\">�ߋ����O</a>]\n" if ($pastkey);
	print "[<a href=\"$script?mode=admin\">�Ǘ��p</a>]\n";
	print "<hr width=\"90%\"></div>\n";

	# ���e�t�H�[��
	&form();
	print "<center><br>\n";

	# �L���W�J
	$rescount = 0;
	$i=0;
	$flag=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	$top = <IN>;
	while (<IN>) {
		($no,$reno,$date,$name,$mail,$sub,$comment,$url,$host,$pw,$color,$tail,$w,$h,$chk) = split(/<>/);

		if ($reno eq "") { $i++;}
		else{$rescount++;}
		if ($i < $page + 1) {$rescount = 0; next; }
		if ($i > $page + $p_log) {$rescount = 0; next; }

		# �薼�̒���
		if (length($sub) > $sub_len*2) {
			$sub = substr($sub,0,$sub_len*2);
			$sub .= "...";
		}

		if ($mail) { $name = "<a href=\"mailto:$mail\">$name</a>"; }
		if ($home_icon && $url) { $url = "<a href=\"http://$url\" target='_blank'><img src=\"$imgurl$IconHome\" border=0 align=top alt='HomePage'></a>"; }
		elsif (!$home_icon && $url) { $url = "&lt;<a href=\"http://$url\" target='_blank'>HOME</a>&gt;"; }

		if (!$reno && $flag) {
			print "</TD></TR></TABLE><br><br>\n";
			$flag=1;
		}
		if (!$reno) {
			print "<TABLE BORDER=1 WIDTH='90%' BGCOLOR=\"$tbl_color\" CELLSPACING=0 CELLPADDING=2><TR><TD>\n";
			$rescount = 0;
			$flag=1;
		}

		if ($reno) { print "<hr noshade size=1 width='85%'>\n"; }
		print "<table border=0 cellpadding=2><tr>\n";
		if ($reno) { print "<td rowspan=2 width=40><br></td>"; }

		print "<td valign=top nowrap><font color=\"$sub_color\"><b>$sub</b></font>�@";

		if (!$reno) { print "���e�ҁF<b>$name</b> ���e���F$date "; }
		else { print "<b>$name</b> - $date "; }

		print "<font color=\"$sub_color\">No.$no</font></td>";
		print "<td valign=top nowrap> &nbsp; $url </td><td valign=top>\n";

		if (!$reno) {
			print "<form action=\"$script\">\n";
			print "<input type=hidden name=mode value=res>\n";
			print "<input type=hidden name=no value=\"$no\">\n";
			print "<input type=submit value='�ԐM'></td></form>\n";
		} else {
			print "<br></td>\n";
		}

		print "</tr></table><table border=0 cellpadding=5><tr>\n";
		if ($reno) { print "<td width=32><br></td>\n"; }

		print "<td>";
		if (!$reno) { print "<blockquote>\n"; }

		# ���������N
		if ($autolink) { &auto_link($comment); }
		if ($imgpoint == 1) {
			$ipt="align=left hspace=18";
		} else {
			$ipt="";
			print "<font color=\"$color\">$comment</font>";
		}

		# �Y�t�t�@�C�������݂���ꍇ
		if ($tail eq ".gif" || $tail eq ".jpg" || $tail eq ".png") {
			if ($ImageCheck && $chk != 1) {
				print "<p><img src=\"$imgurl$IconSoon\">\n";
			} else {
				if ($w && $h) { $wh="width=$w height=$h"; }
				else { $wh=""; }
				print "<p><a href=\"$imgurl$no$tail\" target='_blank'><img src=\"$imgurl$no$tail\" border=0 $ipt $wh></a>\n";
			}
		} elsif ($tail) {
			print "<p><a href=\"$imgurl$no$tail\"><img src=\"$imgurl$IconClip\" border=0 alt='Download:$no$tail'></a> <b>$no$tail</b>\n";
		}

		print "<font color=\"$color\">$comment</font><br clear=all>" if ($imgpoint == 1);
		if (!$reno) { print "</blockquote>\n"; }
		print "</td></tr></table>\n";
		if($rescount >= $maxres)
		{
			print '<hr noshade size=1 width="85%">';
			print '<table border=0 cellpadding=2><tr>';
			print '<td rowspan=2 width=40><br></td><td valign=top nowrap><font color="#880000"><b>�X���������</b></font>�@<b>�X���b�h�X�g�b�v����</b> - Nothing <font color="#000000">No.Nothing</font></td><td valign=top nowrap> &nbsp;  </td><td valign=top>';
			print '<br></td>';
			print '</tr></table><table border=0 cellpadding=5><tr>';
			print '<td width=32><br></td>';
			print '<td><font color="#000000">�X���b�h�̃��X����𒴂��Ă��܂��B���̘b��𑱂���ꍇ�́A�V�X���b�h�𗧂��グ�ĉ������B</font><br clear=all></td></tr></table>';
		}
	}
	print "</TD></TR></TABLE></center>\n";
	close(IN);

	$next = $page + $p_log;
	$back = $page - $p_log;

	$p_flag=0;
	print "<p><blockquote><table cellpadding=0 cellspacing=0><tr>\n";
	if ($back >= 0) {
		$p_flag=1;
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=page value=\"$back\">\n";
		print "<input type=submit value=\"�O��$p_log��\"></td></form>\n";
	}
	if ($next < $i) {
		$p_flag=1;
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=page value=\"$next\">\n";
		print "<input type=submit value=\"����$p_log��\"></td></form>\n";
	}
	# �y�[�W�ړ��{�^���\��
	if ($p_flag) {
		print "<td width=10></td><td>\n";
		$x=1;
		$y=0;
		while ($i > 0) {
			if ($page == $y) { print "<b>[$x]</b>\n"; }
			else { print "[<a href=\"$script?page=$y\">$x</a>]\n"; }
			$x++;
			$y = $y + $p_log;
			$i = $i - $p_log;
		}
		print "</td>\n";
	}
	print "</tr></table></blockquote>\n";
	print "<div align=center>\n";
	print "<form action=\"$script\" method=\"POST\">\n";
	print "<font color=\"$t_color\">- �ȉ��̃t�H�[�����玩���̓��e�L�����C���E�폜���邱�Ƃ��ł��܂� -</font><br>\n";
	print "���� <select name=mode>\n";
	print "<option value=usr_edt>�C��\n";
	print "<option value=usr_del>�폜</select>\n";
	print "�L��No <input type=text name=no size=3>\n";
	print "�Ï؃L�[ <input type=password name=pwd size=4 maxlength=30>\n";
	print "<input type=submit value=\"���M\"></form>\n";

	# ���쌠�\�����i�폜���ϕs�j
	print "$banner2<p><!-- $ver -->\n";
	print "<span style='font-size:10px;font-family:Verdana,Helvetica,Arial'>\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Joyful Note</a> -\n";
	print "</span></div>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �X���b�h�r���[�\��
#-------------------------------------------------
sub thview {
	local($ipt,$wh,$i,$flag,$rescount,$f,$no,$reno,$date,$name,$mail,$sub,$com,$url);

	# �w�b�_���o��
	&header;

	# �J�E���^����
	if ($counter) { &counter; }

	# ���O��ǂݍ���
	$f=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	$top = <IN>;
	
	# �֘A�L���o��
	print "<BR>";
	print "[<a href=\"javascript:history.back()\">�߂�</a>]<p>\n";
	print "- �ȉ��́A�L��NO. <B>$in{'no'}</B> �̃X���b�h\�\\���ł� -<hr>\n";
	print "<center><br>\n";
	$flag=0;
	while (<IN>) {
		($no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color,$tail,$w,$h,$chk) = split(/<>/);

		if ($in{'no'} == $no && $reno) { $f++; }
		if ($in{'no'} == $no || $in{'no'} == $reno) {
			if ($in{'no'} == $no) { $resub = $sub; }
			if ($reno eq "") { $i++;}
			else{$rescount++;}
			if ($i < $page + 1) {$rescount = 0; next; }
			if ($i > $page + $p_log) {$rescount = 0; next; }
		
			# �薼�̒���
			if (length($sub) > $sub_len*2) {
				$sub = substr($sub,0,$sub_len*2);
				$sub .= "...";
			}
			if ($mail) { $name = "<a href=\"mailto:$mail\">$name</a>"; }
			if ($home_icon && $url) { $url = "<a href=\"http://$url\" target='_blank'><img src=\"$imgurl$IconHome\" border=0 align=top alt='HomePage'></a>"; }
			elsif (!$home_icon && $url) { $url = "&lt;<a href=\"http://$url\" target='_blank'>HOME</a>&gt;"; }
			
			if (!$reno && $flag) {
				print "</TD></TR></TABLE><br><br>\n";
				$flag=1;
			}
			if (!$reno) {
				print "<TABLE BORDER=1 WIDTH='90%' BGCOLOR=\"$tbl_color\" CELLSPACING=0 CELLPADDING=2><TR><TD>\n";
				$rescount = 0;
				$flag=1;
			}
			
			if ($reno) { print "<hr noshade size=1 width='85%'>\n"; }
			print "<table border=0 cellpadding=2><tr>\n";
			if ($reno) { print "<td rowspan=2 width=40><br></td>"; }
			
			print "<td valign=top nowrap><font color=\"$sub_color\"><b>$sub</b></font>�@";
			
			if (!$reno) { print "���e�ҁF<b>$name</b> ���e���F$date "; }
			else { print "<b>$name</b> - $date "; }
			
			print "<font color=\"$sub_color\">No.$no</font></td>";
			print "<td valign=top nowrap> &nbsp; $url </td><td valign=top>\n";
			print "<br></td>\n";
			
			print "</tr></table><table border=0 cellpadding=5><tr>\n";
			if ($reno) { print "<td width=32><br></td>\n"; }
			
			print "<td>";
			if (!$reno) { print "<blockquote>\n"; }
			
			# ���������N
			if ($autolink) { &auto_link($com); }
			if ($imgpoint == 1) {
				$ipt="align=left hspace=18";
			} else {
				$ipt="";
				print "<font color=\"$color\">$com</font>";
			}
			
			# �Y�t�t�@�C�������݂���ꍇ
			if ($tail eq ".gif" || $tail eq ".jpg" || $tail eq ".png") {
				if ($ImageCheck && $chk != 1) {
					print "<p><img src=\"$imgurl$IconSoon\">\n";
				} else {
					if ($w && $h) { $wh="width=$w height=$h"; }
					else { $wh=""; }
					print "<p><a href=\"$imgurl$no$tail\" target='_blank'><img src=\"$imgurl$no$tail\" border=0 $ipt $wh></a>\n";
				}
			} elsif ($tail) {
				print "<p><a href=\"$imgurl$no$tail\"><img src=\"$imgurl$IconClip\" border=0 alt='Download:$no$tail'></a> <b>$no$tail</b>\n";
			}
			
			print "<font color=\"$color\">$com</font><br clear=all>" if ($imgpoint == 1);
			if (!$reno) { print "</blockquote>\n"; }
			print "</td></tr></table>\n";
			if($rescount >= $maxres)
			{
				print '<hr noshade size=1 width="85%">';
				print '<table border=0 cellpadding=2><tr>';
			print '<td rowspan=2 width=40><br></td><td valign=top nowrap><font color="#880000"><b>�X���������</b></font>�@<b>�X���b�h�X�g�b�v����</b> - Nothing <font color="#000000">No.Nothing</font></td><td valign=top nowrap> &nbsp;  </td><td valign=top>';
				print '<br></td>';
				print '</tr></table><table border=0 cellpadding=5><tr>';
				print '<td width=32><br></td>';
				print '<td><font color="#000000">�X���b�h�̃��X����𒴂��Ă��܂��B���̘b��𑱂���ꍇ�́A�V�X���b�h�𗧂��グ�ĉ������B</font><br clear=all></td></tr></table>';
			}
		}
	}
	print "</TD></TR></TABLE></center>\n";
	close(IN);
	if ($f) { &error("�s���ȃX���b�h�\���v���ł�"); }
	if ($flag) { print "</blockquote>\n"; }
	print "<hr>\n";
	if($rescount < $maxres)
	{
		# �^�C�g����
		if ($resub !~ /^Re\:/) { $resub = "Re\: $resub"; }
		
		print "<a name=\"RES\"></a>\n";
		&form("res","","","","","",$resub,"","","","","");
		print "</body>\n</html>\n";
	}
	
	print "<div align=center>\n";
	print "<form action=\"$script\" method=\"POST\">\n";
	print "<font color=\"$t_color\">- �ȉ��̃t�H�[�����玩���̓��e�L�����C���E�폜���邱�Ƃ��ł��܂� -</font><br>\n";
	print "���� <select name=mode>\n";
	print "<option value=usr_edt>�C��\n";
	print "<option value=usr_del>�폜</select>\n";
	print "�L��No <input type=text name=no size=4>\n";
	print "�Ï؃L�[ <input type=password name=pwd size=8 maxlength=30>\n";
	print "<input type=submit value=\"���M\"></form>\n";
	
	exit;
}

#-------------------------------------------------
#  �X���b�h���X�g�\��
#-------------------------------------------------
sub list {
	local($ipt,$wh,$i,$flag,$rescount,$thcount);

	# �w�b�_���o��
	&header;

	# �J�E���^����
	if ($counter) { &counter; }

	# �^�C�g����
	print "<div align='center'>\n";
	if ($banner1 ne "<!-- �㕔 -->") { print "$banner1<p>\n"; }
	if ($t_img eq '') {
		print "<b style=\"font-size:$t_size;color:$t_color;\">$title</b>\n";
	} else {
		print "<img src=\"$t_img\" width=\"$t_w\" height=\"$t_h\" alt=\"$title\">\n";
	}

	# ���j���[��
	print "<hr width=\"90%\">\n";
	print "[<a href=\"$script\">�ʏ�\�\\���ɖ߂�</a>]\n";
	print "[<a href=\"$script?mode=howto\">���ӎ���</a>]\n";
	print "[<a href=\"$script?mode=find\">���[�h����</a>]\n";
	print "[<a href=\"$script?mode=past\">�ߋ����O</a>]\n" if ($pastkey);
	print "[<a href=\"$script?mode=admin\">�Ǘ��p</a>]\n";
	print "<hr width=\"90%\"></div>\n";
	
	# �L���W�J
	print "<div align='center'>\n";
	$rescount = 0;
	$thcount = 0;
	$i=0;
	$flag=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	print "<TABLE RULES=\"all\" BORDER=\"3\">\n<TR><TD>�X���b�h</TD><TD>�����e��</TD><TD>�ŏI���e��</TD><TD>�ŏI���e��</TD><TD>���X��</TD></TR>\n";
	$top = <IN>;
	while (<IN>) {
		$prename = $name;
		$predate = $date;
		($no,$reno,$date,$name,$mail,$sub,$comment,$url,$host,$pw,$color,$tail,$w,$h,$chk) = split(/<>/);
		if (!$reno)
		{
			if($thcount > 0)
			{
				print "<TD>$prename</TD><TD>$predate</TD><TD>$rescount</TD></TR>\n";
			}
			print "<TR><TD><a href=\"$script?mode=thview&no=$no\">$sub</a></TD><TD>$name</TD>\n";
			$rescount = 0;
			$thcount++;
		}
		else
		{
			$rescount++;
		}
	}
	if($thcount > 0)
	{
		print "<TD>$prename</TD><TD>$predate</TD><TD>$rescount</TD></TR>\n";
	}
	print "</TABLE>\n";
	print "</div>\n";
	close(IN);
	
	# ���쌠�\�����i�폜���ϕs�j
	print "<div align=center>\n";
	print "$banner2<p><!-- $ver -->\n";
	print "<span style='font-size:10px;font-family:Verdana,Helvetica,Arial'>\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Joyful Note</a> -\n";
	print "</span></div>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  ���e�L����t
#-------------------------------------------------
sub regist {
	local($top,$ango,$f,$match,$tail,$W,$H,@lines,@new,@tmp, $rescount);

	# �t�H�[�����̓`�F�b�N
	&form_check;
	$rescount = 0;
	# �֎~���[�h�`�F�b�N
	if ($deny_word) {
		&deny_word($in{'name'});
		&deny_word($in{'email'});
		&deny_word($in{'comment'});
	}

	# �N�b�L�[�𔭍s
	&set_cookie($in{'name'},$in{'email'},$in{'url'},$in{'pwd'},$in{'icon'},$in{'color'});

	# �t�@�C�����b�N
	if ($lockkey) { &lock; }

	# ���O���J��
	open(IN,"$logfile") || &error("Open Error: $logfile");
	@lines = <IN>;
	close(IN);

	# �L��NO����
	$top = shift(@lines);
	local($no,$ip,$time2) = split(/<>/, $top);
	$no++;

	# �A�����e�`�F�b�N
	if ($addr eq $ip && $wait > $times - $time2)
		{ &error("�A�����e�͂������΂炭���Ԃ������ĉ�����"); }

	# �폜�L�[���Í���
	if ($in{'pwd'} ne "") { $ango = &encrypt($in{'pwd'}); }

	# �t�@�C���Y�t����
	if ($in{'upfile'}) { ($tail,$W,$H) = &upload; }

	# sage�`�F�b�N
	if($in{'email'} eq "sage")
	{
		$topsort = 0;
	}

	# �e�L���̏ꍇ
	if ($in{'reno'} eq "") {
		$i=0;
		$stop=0;
		foreach (@lines) {
			($no2,$reno2,$d,$n,$m,$s,$com,$u,$ho,$p,$c,$tail2,$w,$h,$chk) = split(/<>/);
			$i++;
			if ($i > $max-1 && $reno2 eq "") { $stop=1; }
			if (!$stop) { push(@new,$_); }
			else {
				if ($pastkey) { push(@data,$_); }
				if (-e "$imgdir$no2$tail2") { unlink("$imgdir$no2$tail2"); }
			}
		}
		unshift(@new,"$no<><>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$ango<>$in{'color'}<>$tail<>$W<>$H<>0<>$addr\n");
		unshift(@new,"$no<>$addr<>$times<>\n");

		# �ߋ����O�X�V
		if ($data[0]) { &pastlog; }

		# �X�V
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);

	# ���X�L���̏ꍇ�F�g�b�v�\�[�g����
	} elsif ($in{'reno'} && $topsort) {

		$f=0;
		$match=0;
		@new=();
		@tmp=();
		foreach (@lines) {
			($no2,$reno2) = split(/<>/);

			if ($in{'reno'} eq $no2) {
				if ($reno2) { $f++; last; }
				$match=1;
				push(@new,$_);

			} elsif ($in{'reno'} eq $reno2) {
				$rescount++;
				if($rescount >= $maxres){last;}
				push(@new,$_);
			} elsif ($match == 1 && $in{'reno'} ne $reno2) {
				$match=2;
				push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$ango<>$in{'color'}<>$tail<>$W<>$H<>0<>$addr\n");
				push(@tmp,$_);

			} else { push(@tmp,$_); }
		}
		if ($rescount >= $maxres) { &error("�ő�ԐM����$maxres�𒴂��Ă��܂��B�V�X���𗧂ĂĂ�������"); };
		if ($f || !$match) { &error("�s���ȕԐM�v���ł�"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$ango<>$in{'color'}<>$tail<>$W<>$H<>0<>$addr\n");
		}
		push(@new,@tmp);

		# �X�V
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);

	# ���X�L���̏ꍇ�F�g�b�v�\�[�g�Ȃ�
	} else {
		$f=0;
		$match=0;
		@new=();
		foreach (@lines) {
			($no2,$reno2) = split(/<>/);

			if ($match == 0 && $in{'reno'} eq $no2) {
				if ($reno2) { $f++; last; }
				$match=1;

			} elsif ($in{'reno'} eq $reno2) {
				$rescount++;
				if($rescount >= $maxres){last;}
			} elsif ($match == 1 && $in{'reno'} ne $reno2) {
				$match=2;
				push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$ango<>$in{'color'}<>$tail<>$W<>$H<>0<>$addr\n");
			}
			push(@new,$_);
		}
		if ($rescount >= $maxres) { &error("�ő�ԐM����$maxres�𒴂��Ă��܂��B�V�X���𗧂ĂĂ�������"); };
		if ($f || !$match) { &error("�s���ȕԐM�v���ł�"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$ango<>$in{'color'}<>$tail<>$W<>$H<>0<>$addr\n");
		}

		# �X�V
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);
	}

	# ���b�N����
	if ($lockkey) { &unlock; }

	# ���[������
	if ($mailing == 1 && $in{'email'} ne $mailto) { &mail_to; }
	elsif ($mailing == 2) { &mail_to; }

	# �����[�h
	if ($location) {
		if ($ENV{'PERLXS'} eq "PerlIS") {
			print "HTTP/1.0 302 Temporary Redirection\r\n";
			print "Content-type: text/html\n";
		}
		print "Location: $location?\n\n";

	} else {
		&header;
		print "<div align=center><hr width=400>\n";
		print "<h3>���e�͐���ɏ�������܂���</h3>\n";
		print "<form action=\"$script\">\n";
		print "<input type=submit value='�f���֖߂�'></form>\n";
		print "<hr width=400></div>\n</body></html>\n";
	}
	exit;
}

#-------------------------------------------------
#  �摜�A�b�v���[�h
#-------------------------------------------------
sub upload {
	local($macbin,$fname,$flag,$upfile,$imgfile,$tail,$W,$W2,$H,$H2);

	# �摜����
	$macbin=0;
	foreach (@in) {
		if (/(.*)Content-type:(.*)/i) { $tail=$2; }
		if (/(.*)filename=\"(.*)\"/i) { $fname=$2; }
		if (/application\/x-macbinary/i) { $macbin=1; }
	}
	$tail =~ s/\r//g;
	$tail =~ s/\n//g;

	# �t�@�C���`����F��
	$flag=0;
	if ($tail =~ /image\/gif/i && $gif) { $tail=".gif"; $flag=1; }
	if ($tail =~ /image\/p?jpeg/i && $jpeg) { $tail=".jpg"; $flag=1; }
	if ($tail =~ /image\/x-png/i && $png) { $tail=".png"; $flag=1; }
	if ($tail =~ /text\/plain/i && $text) { $tail=".txt"; $flag=1; }
	if ($tail =~ /lha/i && $lha) { $tail=".lzh"; $flag=1; }
	if ($tail =~ /zip/i && $zip) { $tail=".zip"; $flag=1; }
	if ($tail =~ /pdf/i && $pdf) { $tail=".pdf"; $flag=1; }
	if ($tail =~ /audio\/.*mid/i && $midi) { $tail=".mid"; $flag=1; }
	if ($tail =~ /msword/i && $word) { $tail=".doc"; $flag=1; }
	if ($tail =~ /msword/i && $word) { $tail=".docx"; $flag=1; }
	if ($tail =~ /ms-excel/i && $excel) { $tail=".xls"; $flag=1; }
	if ($tail =~ /ms-excel/i && $excel) { $tail=".xlsx"; $flag=1; }
	if ($tail =~ /ms-powerpoint/i && $ppt) { $tail=".ppt"; $flag=1; }
	if ($tail =~ /ms-powerpoint/i && $ppt) { $tail=".pptx"; $flag=1; }
	if ($tail =~ /audio\/.*realaudio/i && $ram) { $tail=".ram"; $flag=1; }
	if ($tail =~ /application\/.*realmedia/i && $rm) { $tail=".rm"; $flag=1; }
	if ($tail =~ /video\/.*mpeg/i && $mpeg) { $tail=".mpg"; $flag=1; }
	if ($tail =~ /audio\/.*mpeg/i && $mp3) { $tail=".mp3"; $flag=1; }

	if (!$flag) {
		if ($fname =~ /\.gif$/i && $gif) { $tail=".gif"; $flag=1; }
		if ($fname =~ /\.jpe?g$/i && $jpeg) { $tail=".jpg"; $flag=1; }
		if ($fname =~ /\.png$/i && $png) { $tail=".png"; $flag=1; }
		if ($fname =~ /\.lzh$/i && $lha) { $tail=".lzh"; $flag=1; }
		if ($fname =~ /\.txt$/i && $text) { $tail=".txt"; $flag=1; }
		if ($fname =~ /\.zip$/i && $zip) { $tail=".zip"; $flag=1; }
		if ($fname =~ /\.pdf$/i && $pdf) { $tail=".pdf"; $flag=1; }
		if ($fname =~ /\.mid$/i && $midi) { $tail=".mid"; $flag=1; }
		if ($fname =~ /\.doc$/i && $word) { $tail=".doc"; $flag=1; }
		if ($fname =~ /\.docx$/i && $word) { $tail=".docx"; $flag=1; }
		if ($fname =~ /\.xls$/i && $excel) { $tail=".xls"; $flag=1; }
		if ($fname =~ /\.xlsx$/i && $excel) { $tail=".xlsx"; $flag=1; }
		if ($fname =~ /\.ppt$/i && $ppt) { $tail=".ppt"; $flag=1; }
		if ($fname =~ /\.pptx$/i && $ppt) { $tail=".pptx"; $flag=1; }
		if ($fname =~ /\.ram$/i && $ram) { $tail=".ram"; $flag=1; }
		if ($fname =~ /\.rm$/i && $rm) { $tail=".rm"; $flag=1; }
		if ($fname =~ /\.mpe?g$/i && $mpeg) { $tail=".mpg"; $flag=1; }
		if ($fname =~ /\.mp3$/i && $mp3) { $tail=".mp3"; $flag=1; }
		if ($fname =~ /\.kif$/i && $kif) { $tail=".kif"; $flag=1; }
		if ($fname =~ /\.ki2$/i && $ki2) { $tail=".ki2"; $flag=1; }
		if ($fname =~ /\.csa$/i && $csa) { $tail=".csa"; $flag=1; }
		if ($fname =~ /\.bod$/i && $bod) { $tail=".bod"; $flag=1; }
		if ($fname =~ /\.gbd$/i && $gbd) { $tail=".gbd"; $flag=1; }
		if ($fname =~ /\.gam$/i && $gam) { $tail=".gam"; $flag=1; }
	}

	# �A�b�v���[�h���s����
	if (!$flag || !$fname) {
		if (!$clip_err) { return; }
		else { &error("�A�b�v���[�h�ł��܂���"); }
	}

	$upfile = $in{'upfile'};

	# �}�b�N�o�C�i���΍�
	if ($macbin) {
		$length = substr($upfile,83,4);
		$length = unpack("%N",$length);
		$upfile = substr($upfile,128,$length);
	}

	# �Y�t�f�[�^����������
	$imgfile = "$imgdir$no$tail";
	open(OUT,">$imgfile") || &error("�A�b�v���[�h���s");
	binmode(OUT);
	binmode(STDOUT);
	print OUT $upfile;
	close(OUT);

	chmod (0666, $imgfile);

	# �摜�T�C�Y�擾
	if ($tail eq ".jpg") { ($W, $H) = &JpegSize($imgfile); }
	elsif ($tail eq ".gif") { ($W, $H) = &GifSize($imgfile); }
	elsif ($tail eq ".png") { ($W, $H) = &PngSize($imgfile); }

	# �摜�\���k��
	if ($W > $MaxW || $H > $MaxH) {
		$W2 = $MaxW / $W;
		$H2 = $MaxH / $H;
		if ($W2 < $H2) { $key = $W2; }
		else { $key = $H2; }
		$W = int ($W * $key) || 1;
		$H = int ($H * $key) || 1;
	}

	return ($tail,$W,$H);
}

#-------------------------------------------------
#  �ԐM�t�H�[��
#-------------------------------------------------
sub res_form {
	local($f,$no,$reno,$date,$name,$mail,$sub,$com,$url);

	# �w�b�_���o��
	&header;

	# ���O��ǂݍ���
	$f=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	$top = <IN>;

	# �֘A�L���o��
	print "[<a href=\"javascript:history.back()\">�߂�</a>]<p>\n";
	print "- �ȉ��́A�L��NO. <B>$in{'no'}</B> �Ɋւ��� <a href='#RES'>�ԐM�t�H�[��</a> �ł� -<hr>\n";
	$flag=0;
	while (<IN>) {
		($no,$reno,$date,$name,$mail,$sub,$com,$url) = split(/<>/);
		if (!$reno) { $com = "<blockquote>$com</blockquote>"; }

		if ($in{'no'} == $no && $reno) { $f++; }
		if ($in{'no'} == $no || $in{'no'} == $reno) {
			if ($in{'no'} == $no) { $resub = $sub; }
			if ($url) { $url = "&lt;<a href=\"http://$url\">HOME</a>&gt;"; }
			if ($reno && !$flag) { print "<blockquote>\n"; $flag=1; }
			print "<font color=$sub_color><b>$sub</b></font> ���e�ҁF<b>$name</b> ���e���F$date $url <font color=$sub_color>No.$no</font><br>$com<p>\n";
		}
	}
	close(IN);
	if ($f) { &error("�s���ȕԐM�v���ł�"); }
	if ($flag) { print "</blockquote>\n"; }
	print "<hr>\n";

	# �^�C�g����
	if ($resub !~ /^Re\:/) { $resub = "Re\: $resub"; }

	print "<a name=\"RES\"></a>\n";
	&form("res","","","","","",$resub,"","","","","");
	print "</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �f�R�[�h����
#-------------------------------------------------
sub decode {
	local($key,$val);
	undef(%in);

	&ReadParse;
	while ( ($key,$val) = each(%in) ) {

		next if ($key eq "upfile");

		# �V�t�gJIS�R�[�h�ϊ�
		&jcode'convert(*val, "sjis", "", "z");

		# �^�O����
		$val =~ s/&/&amp;/g;
		$val =~ s/"/&quot;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;

		# ���s����
		$val =~ s/\r\n/<br>/g;
		$val =~ s/\r/<br>/g;
		$val =~ s/\n/<br>/g;

		$in{$key} = $val;
	}
	$mode = $in{'mode'};
	$page = $in{'page'};
	$in{'url'} =~ s/^https\:\/\///;
	$in{'url'} =~ s/^http\:\/\///;
	if ($in{'sub'} eq "") { $in{'sub'} = "����"; }
}

#-------------------------------------------------
#  ���ӎ���
#-------------------------------------------------
sub howto {
	if ($in_email) {
		$eml_msg = "�L���𓊍e�����ł̕K�{���͍��ڂ�<b>�u���Ȃ܂��v�u�d���[���v�u���b�Z�[�W�v</b>�ł��B�t�q�k�A�薼�A�폜�L�[�͔C�ӂł��B";
	} else {
		$eml_msg = "�L���𓊍e�����ł̕K�{���͍��ڂ�<b>�u���Ȃ܂��v</b>��<b>�u���b�Z�[�W�v</b>�ł��B�d���[���A�t�q�k�A�薼�A�폜�L�[�͔C�ӂł��B";
	}

	$maxkb = int ($cgi_lib'maxdata / 1024);
	if ($gif) { $FILE .= "GIF, "; }
	if ($jpeg) { $FILE .= "JPEG, "; }
	if ($png) { $FILE .= "PNG, "; }
	if ($text) { $FILE .= "TEXT, "; }
	if ($lha) { $FILE .= "LHA, "; }
	if ($zip) { $FILE .= "ZIP, "; }
	if ($pdf) { $FILE .= "PDF, "; }
	if ($midi) { $FILE .= "MIDI, "; }
	if ($word) { $FILE .= "WORD, "; }
	if ($excel) { $FILE .= "EXCEL, "; }
	if ($ppt) { $FILE .= "POWERPOINT, "; }
	if ($rm) { $FILE .= "RM, "; }
	if ($ram) { $FILE .= "RAM, "; }
	if ($mpeg) { $FILE .= "MPEG, "; }
	if ($mp3) { $FILE .= "MP3, "; }
	if ($kif) { $FILE .= "KIF, "; }
	if ($ki2) { $FILE .= "KI2, "; }
	if ($csa) { $FILE .= "CSA, "; }
	if ($bod) { $FILE .= "BOD, "; }
	if ($gbd) { $FILE .= "GBD, "; }
	if ($gam) { $FILE .= "GAM, "; }
	$FILE =~ s/\, $//;

	&header;
	print <<"HTML";
[<a href="$script?">�f���ɂ��ǂ�</a>]
<table width="100%">
<tr><th bgcolor="#880000">
  <font color="#FFFFFF">�f���̗��p��̒���</font>
</th></tr></table>
<p><center>
<table width="90%" border=1 cellpadding=10>
<tr><td bgcolor="$tbl_color">
<OL>
<li>���̌f����<b>�N�b�L�[�Ή�</b>�ł��B�P�x�L���𓊍e���������ƁA���Ȃ܂��A�d���[���A�t�q�k�A�폜�L�[�̏��͂Q��ڈȍ~�͎������͂���܂��B�i���������p�҂̃u���E�U���N�b�L�[�Ή��̏ꍇ�j<p>
<li>�摜�Ȃǂ̃o�C�i���[�t�@�C�����A�b�v���[�h���邱�Ƃ��\\�ł��B
<p>
  <ul>
  <li>�Y�t�\\�t�@�C�� : $FILE
  <li>�ő哊�e�f�[�^�� : $maxkb KB
  <li>�摜�͉�$MaxW�s�N�Z���A�c$MaxH�s�N�Z���𒴂���Ək���\\������܂��B
  </ul>
<p>
<li>���e���e�ɂ́A<b>�^�O�͈�؎g�p�ł��܂���B</b><p>
<li>$eml_msg<p>
<li>�L���ɂ́A<b>���p�J�i�͈�؎g�p���Ȃ��ŉ������B</b>���������̌����ƂȂ�܂��B<p>
<li>�L���̓��e����<b>�u�폜�L�[�v</b>�Ƀp�X���[�h�i�p������8�����ȓ��j�����Ă����ƁA���̋L���͎���<b>�폜�L�[</b>�ɂ���č폜���邱�Ƃ��ł��܂��B<p>
<li>�L���̕ێ�������<b>�ő� $max��</b>�ł��B����𒴂���ƌÂ����Ɏ����폜����܂��B<p>
<li>�����̋L����<b>�u�ԐM�v</b>�����邱�Ƃ��ł��܂��B�e�L���̏㕔�ɂ���<b>�u�ԐM�v</b>�{�^���������ƕԐM�p�t�H�[��������܂��B<p>
<li>�ߋ��̓��e�L������<b>�u�L�[���[�h�v�ɂ���ĊȈՌ������ł��܂��B</b>�g�b�v���j���[��<a href="$script?mode=find">�u���[�h�����v</a>�̃����N���N���b�N����ƌ������[�h�ƂȂ�܂��B<p>
<br>
</OL>
</td></tr></table>
<br>
<table width="100%">
<tr><th bgcolor="#880000">
  <font color="#FFFFFF">�Ǘ��K��</font>
</th></tr></table>
<br>
<table width="90%" border=1 cellpadding=10>
<tr><td bgcolor="$tbl_color">
</td></tr></table>
</center>
</body>
</html>
HTML
	exit;
}

#-------------------------------------------------
#  ���[�h��������
#-------------------------------------------------
sub find {
	&header;
	print <<"EOM";
[<a href="$script?">�f���ɖ߂�</a>]
<p>
<ul>
  <li>����������<b>�L�[���[�h</b>����͂��A�u�����v�u�\\���v��I�����Č����{�^���������ĉ������B
  <li>�L�[���[�h�́u���p�X�y�[�X�v�ŋ�؂��ĕ����w�肷�邱�Ƃ��ł��܂��B
<p><form action="$script" method="POST">
<input type=hidden name=mode value="find">
�L�[���[�h�F<input type=text name=word size=30 value="$in{'word'}">
�����F<select name=cond>
EOM
	if (!$in{'cond'}) { $in{'cond'} = "AND"; }
	foreach ("AND", "OR") {
		if ($in{'cond'} eq "$_") {
			print "<option value=\"$_\" selected>$_\n";
		} else {
			print "<option value=\"$_\">$_\n";
		}
	}
	print "</select>\n";
	print "�\\���F<select name=view>\n";
	if ($in{'view'} eq "") { $in{'view'} = $p_log; }
	foreach (5,10,15,20) {
		if ($in{'view'} == $_) {
			print "<option value=\"$_\" selected>$_��\n";
		} else {
			print "<option value=\"$_\">$_��\n";
		}
	}
	print "</select>\n";
	print "<input type=submit value='����'></form>\n</ul>\n";

	# ���[�h�����̎��s�ƌ��ʕ\��
	if ($in{'word'} ne "") {

		# ���͓��e�𐮗�
		$in{'word'} =~ s/�@/ /g;
		@pairs = split(/\s+/, $in{'word'});

		# �t�@�C����ǂݍ���
		@new=();
		open(IN,"$logfile") || &error("Open Error : $logfile");
		$top = <IN>;
		while (<IN>) {
			$flag=0;
			foreach $pair (@pairs) {
;				@indexArray = split/<>/;
				
				#@indexArray = splice(@indexArray, 8, 1);
				$indexArray[8] = "";
				$indexArray[9] = "";
				$indexArray[15] = "";
				$indexValue = "";
				foreach $arrayValue(@indexArray)
				{
					$indexValue = $indexValue . $arrayValue . "<>";
				}
				
				
				if (index($indexValue, $pair) >= 0) {
					$flag=1;
					if ($in{'cond'} eq 'OR') { last; }
				} else {
					if ($in{'cond'} eq 'AND') { $flag=0; last; }
				}
			}
			if ($flag) { push(@new,$_); }
		}
		close(IN);

		# �����I��
		$count = @new;
		print "�������ʁF<b>$count</b>��\n";
		if ($page eq '') { $page = 0; }
		$end_data = @new - 1;
		$page_end = $page + $in{'view'} - 1;
		if ($page_end >= $end_data) { $page_end = $end_data; }

		$next_line = $page_end + 1;
		$back_line = $page - $in{'view'};

		$enwd = &url_enc($in{'word'});
		if ($back_line >= 0) {
			print "[<a href=\"$script?mode=find&page=$back_line&word=$enwd&view=$in{'view'}&cond=$in{'cond'}\">�O��$in{'view'}��</a>]\n";
		}
		if ($page_end ne "$end_data") {
			print "[<a href=\"$script?mode=find&page=$next_line&word=$enwd&view=$in{'view'}&cond=$in{'cond'}\">����$in{'view'}��</a>]\n";
		}
		print "[<a href=\"$script?mode=find\">������蒼��</a>]\n";

		foreach ($page .. $page_end) {
			($no,$reno,$date,$name,$email,$sub,$com,$url)
						= split(/<>/, $new[$_]);
			if ($email) { $name = "<a href=\"mailto:$email\">$name</a>"; }
			if ($url) { $url = "&lt;<a href=\"http://$url\" target='_top'>HOME</a>&gt;"; }

			if ($reno) { $no = "$reno�ւ̃��X"; }

			# ���ʂ�\��
			print "<hr>[<b>$no</b>] <font color=\"$sub_color\"><b>$sub</b></font>";
			print " ���e�ҁF<b>$name</b> ���e���F$date $url<br>\n";
			print "<blockquote>$com</blockquote>\n";
		}
		print "<hr>\n";
	}
	print "</body></html>\n";
	exit;
}

#-------------------------------------------------
#  �N�b�L�[���s
#-------------------------------------------------
sub set_cookie {
	local(@cook) = @_;
	local($gmt, $cook, @t, @m, @w);

	@t = gmtime(time + 60*24*60*60);
	@m = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	@w = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# ���ەW�������`
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$w[$t[6]], $t[3], $m[$t[4]], $t[5]+1900, $t[2], $t[1], $t[0]);

	# �ۑ��f�[�^��URL�G���R�[�h
	foreach (@cook) {
		s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		$cook .= "$_<>";
	}

	# �i�[
	print "Set-Cookie: JoyfulNote=$cook; expires=$gmt\n";
}

#-------------------------------------------------
#  �N�b�L�[�擾
#-------------------------------------------------
sub get_cookie {
	local($key, $val, *cook);

	# �N�b�L�[���擾
	$cook = $ENV{'HTTP_COOKIE'};

	# �Y��ID�����o��
	foreach ( split(/;/, $cook) ) {
		($key, $val) = split(/=/);
		$key =~ s/\s//g;
		$cook{$key} = $val;
	}

	# �f�[�^��URL�f�R�[�h���ĕ���
	foreach ( split(/<>/, $cook{'JoyfulNote'}) ) {
		s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;

		push(@cook,$_);
	}
	return (@cook);
}

#-------------------------------------------------
#  �G���[����
#-------------------------------------------------
sub error {
	&unlock if ($lockflag);
	&header if (!$headflag);
	open(PROXY,">> $proxy_file") || &error("Open Error: $proxy_file");
	flock(PROXY, 2);
	print PROXY "$date\t$script\t$retstring\t$host\t$addr\t$http_accept\t$user_agent\t$http_referer\t$http_via\t$forwerded_for\t$forwarded_host\t$forwarded\t$in{'name'}\t$mode\n";
	close(PROXY);
	print "<center><hr width=400><h3>ERROR !</h3>\n";
	print "<font color=red>$_[0]</font>\n";
	print "</body></html>\n";
	exit;
}

#-------------------------------------------------
#  �Ǘ����[�h
#-------------------------------------------------
sub admin {
	if ($in{'pass'} eq "") {
		&header;
		print "<center><h4>�p�X���[�h����͂��ĉ�����</h4>\n";
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"del\">\n";
		print "<input type=password name=pass size=8>\n";
		print "<input type=submit value=\" �F�� \"></form>\n";
		print "</center>\n</body></html>\n";
		exit;
	}
	if ($in{'pass'} ne $pass) { &error("�p�X���[�h���Ⴂ�܂�"); }

	&header;
	print "[<a href=\"$script?\">�f���ɖ߂�</a>]\n";
	print "<table width='100%'><tr><th bgcolor=\"#804040\">\n";
	print "<font color=\"#FFFFFF\">�Ǘ����[�h</font>\n";
	print "</th></tr></table>\n";

	# �摜����
	if ($in{'chk'}) {
		@CHK = split(/\0/, $in{'chk'});

		# ���b�N����
		if ($lockkey) { &lock; }

		# �������}�b�`���O���X�V
		@new=();
		open(IN,"$logfile") || &error("Open Error : $logfile");
		$top = <IN>;
		while (<IN>) {
			($no,$reno,$d,$n,$m,$s,$com,$u,$ho,$p,$c,$t,$w,$h,$chk)
								 = split(/<>/);
			foreach $xx (@CHK) {
				if ($no eq $xx) {
					$_ = "$no<>$reno<>$d<>$n<>$m<>$s<>$com<>$u<>$ho<>$p<>$c<>$t<>$w<>$h<>1<>\n";
					last;
				}
			}
			push(@new,$_);
		}
		close(IN);

		# �X�V
		unshift(@new,$top);
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

		# ���b�N����
		if ($lockkey) { &unlock; }
	}
	# �폜����
	if ($in{'del'}) {
		@DEL = split(/\0/, $in{'del'});

		# ���b�N����
		if ($lockkey) { &lock; }

		# �폜�����}�b�`���O���X�V
		@new=();
		open(IN,"$logfile") || &error("Open Error: $logfile");
		$top = <IN>;
		while (<IN>) {
			$flag=0;
			($no,$reno,$d,$n,$m,$s,$com,$u,$ho,$p,$c,$tail,$w,$h,$chk)
								 	= split(/<>/);
			foreach $del (@DEL) {
				if ($no eq $del || $reno eq $del) {
					if (-e "$imgdir$no$tail") {
						unlink("$imgdir$no$tail");
					}
					$flag=1;
					open(DELETE,">> deletelog.cgi") || &error("Open Error: deletelog");
					flock(DELETE, 2);
					print DELETE $_;
					close(DELETE);
					last;
				}
			}
			if ($flag == 0) { push(@new,$_); }
		}
		close(IN);

		# �X�V
		unshift(@new,$top);
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);

		# ���b�N����
		if ($lockkey) { &unlock; }
	}

	# �Ǘ���\��
	if ($page eq "") { $page = 0; }
	print "<p><center><table><tr><td>\n<ul>\n";
	print "<li>�L�����폜����ꍇ�́u�폜�v�̃`�F�b�N�{�b�N�X�Ƀ`�F�b�N�����u���M����v�������ĉ������B\n";
	print "<li>�摜�����s�Ȃ��ꍇ�́u�摜���v�̃`�F�b�N�{�b�N�X�Ƀ`�F�b�N�����u���M����v�������ĉ������B\n";
	print "</ul>\n</td></tr></table>\n";
	print "<form action=\"$script\" method=\"POST\">\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=page value=\"$page\">\n";
	print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
	print "<input type=hidden name=action value=\"$in{'action'}\">\n";
	print "<input type=submit value=\"���M����\">";
	print "<input type=reset value=\"���Z�b�g\">\n";
	print "<p><table border=0 cellspacing=1><tr>\n";
	print "<th nowrap>�폜</th><th nowrap>�L��NO</th><th>���e��</th>";
	print "<th>�^�C�g��</th><th>���e��</th><th>URL</th><th>�R�����g</th>";
	print "<th>�z�X�g��</th><th>�摜<br>(bytes)</th>\n";

	$line=9;
	if ($ImageCheck) { print "<th>�摜<br>����</th>"; $line=10; }

	print "</tr>\n";

	open(IN,"$logfile") || &error("Open Error: $logfile");
	$top = <IN>;
	$i=0;
	while (<IN>) {
		$img_flag=0;
		($no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color,$tail,$w,$h,$chk) = split(/<>/);

		if ($mail) { $name="<a href=\"mailto:$mail\">$name</a>"; }
		($date) = split(/\(/, $date);

		if ($url) { $url = "&lt;<a href=\"http://$url\" target='_top'>Home</a>&gt;"; }
		else { $url = '-'; }

		$com =~ s/<br>//ig;
		$com =~ s/</&lt;/g;
		$com =~ s/>/&gt;/g;
		if (length($com) > 40) {
			$com = substr($com,0,38);
			$com .= "...";
		}
		if (-e "$imgdir$no$tail") {
			if ($tail eq ".gif" || $tail eq ".jpg" || $tail eq ".png") {
				$img_flag = 1;
				$File = "�摜";
			} else { $File = "File"; }
			$clip = "<a href=\"$imgurl$no$tail\" target='_blank'>$File</a>";
			$size = -s "$imgdir$no$tail";
			$all += $size;
		} else {
			$clip = "";
			$size = 0;
		}
		if ($reno eq "") { print "<tr><th colspan=$line><hr></th></tr>\n"; }

		# �`�F�b�N�{�b�N�X
		print "<tr><th><input type=checkbox name=del value=\"$no\"></th>";
		print "<td align=center>$no</td>";
		print "<td>$date</td><th>$sub</th><th>$name</th>";
		print "<td align=center>$url</td><td>$com</td>";
		print "<td>$host</td><td align=center>$clip<br>($size)</td>\n";
		# �摜����
		if ($ImageCheck) {
			if ($img_flag == 1 && $chk == 1) {
				print "<th>OK</th>";
			} elsif ($img_flag == 1 && $chk != 1) {
				print "<th><input type=checkbox name=chk value=$no></th>";
			} else {
				print "<td><br></td>";
			}
		}
		print "</tr>\n";
	}
	close(IN);

	print "<tr><th colspan=$line><hr></th></tr>\n";
	print "</table></form>\n";

	$all = int ($all / 1024);
	print "�y�Y�t�f�[�^���� �F <b>$all</b> KB�z\n";
	print "</center>\n";
	print "</body></html>\n";
	exit;
}

#-------------------------------------------------
#  ���[�U�L���폜
#-------------------------------------------------
sub usr_del {
	if ($in{'no'} eq '' || $in{'pwd'} eq '')
		{ &error("�L��No�܂��͍폜�L�[�����̓����ł�"); }

	# ���b�N����
	if ($lockkey) { &lock; }

	open(IN,"$logfile") || &error("Open Error : $logfile");
	@lines = <IN>;
	close(IN);
	$top = shift(@lines);

	$flag=0;
	foreach (@lines) {
		($no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color,$tail,$w,$h,$chk) = split(/<>/);

		if ($flag == 0 && $in{'no'} eq "$no") {
			if ($pw eq '' && $in{'pwd'} ne $pass) {
				&error("�Y���L���ɂ͍폜�L�[���ݒ肳��Ă��܂���");
			}
			# �폜�L�[���ƍ�
			$match = &decrypt("$in{'pwd'}","$pw");
			if ($match ne 'yes' && $in{'pwd'} ne $pass) { &error("�폜�L�[���Ⴂ�܂�"); }

			# �Y�t�t�@�C���폜
			if (-e "$imgdir$no$tail") { unlink("$imgdir$no$tail"); }

			if ($reno eq "") { $flag=2; }
			else { $flag=1; }
		}
		elsif ($flag == 2 && $in{'no'} eq $reno) {
			if (-e "$imgdir$no$tail") { unlink("$imgdir$no$tail"); }
			next;
		}
		else { push(@new,$_); }
	}
	if ($flag == 0) { &error("�Y���L������������܂���"); }

	# �X�V
	unshift(@new,$top);
	open(OUT,">$logfile") || &error("Write Error : $logfile");
	print OUT @new;
	close(OUT);

	# ���b�N����
	if ($lockkey) { &unlock; }
}

#-------------------------------------------------
#  �L���C������
#-------------------------------------------------
sub usr_edt {
	if ($in{'no'} eq '' || $in{'pwd'} eq '') {
		&error("�L��No�܂��̓p�X���[�h�����̓����ł�");
	}

	if ($in{'action'} eq "edit") {

		# �t�H�[�����̓`�F�b�N
		&form_check;

		# �֎~���[�h�`�F�b�N
		if ($deny_word) {
			&deny_word($in{'name'});
			&deny_word($in{'email'});
			&deny_word($in{'comment'});
		}

		# ���b�N����
		&lock if ($lockkey);
	}

	$flag=0;
	open(IN,"$logfile") || &error("Open Error : $logfile");
	$top = <IN>;
	while (<IN>) {
		($no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color,$tail,$w,$h,$chk,$addr) = split(/<>/);

		if ($in{'no'} == $no) {
			$precomment = $_;
			$pw2 = $pw;
			$flag=1;
			if ($in{'action'} ne "edit") { last; }
			else {
				$_ = "$no<>$reno<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'comment'}<>$in{'url'}<>$host<>$pw<>$in{'color'}<>$tail<>$w<>$h<>$chk<>$addr";
			}
		}
		if ($in{'action'} eq "edit") { push(@new,$_); }
	}
	close(IN);
	if (!$flag) { &error("�Y���̋L������������܂���"); }
	if ($pw2 eq "" && $in{'pwd'} ne $pass) { &error("�p�X���[�h���ݒ肳��Ă��܂���"); }
	$check = &decrypt($in{'pwd'}, $pw2);
	if ($check ne "yes" && $in{'pwd'} ne $pass) { &error("�p�X���[�h���Ⴂ�܂�"); }

	if ($in{'action'} eq "edit") {
		unshift(@new,$top);
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);
		&unlock if ($lockkey);

		if($in{'pwd'} eq $pass){ 
			open(DELETE,">> deletelog.cgi") || &error("Open Error: deletelog");
			flock(DELETE, 2);
			print DELETE $precomment;
			close(DELETE);
		}

		if ($in{'url'}) { $in{'url'} = "<a href=\"http://$in{'url'}\" target=\"_top\">http://$in{'url'}</a>"; }
		if ($in{'email'}) { $in{'email'} = "<a href=\"mailto:$in{'email'}\">$in{'email'}</a>"; }

		&header;
		print "<h4>- �ȉ��̂Ƃ���C�����������܂��� -</h4>\n";
		print "<table>\n";
		print "<tr><td>���O</td><td>�F <b>$in{'name'}</b></td></tr>\n";
		print "<tr><td>e-mail</td><td>�F $in{'email'}</td></tr>\n";
		print "<tr><td>�薼</td><td>�F <b>$in{'sub'}</b></td></tr>\n";
		print "<tr><td>URL</td><td>�F $in{'url'}</td></tr></table>\n";
		print "<blockquote><font color=\"$in{'color'}\">$in{'comment'}</font>\n";
		print "</blockquote>\n";
		print "<form action=\"$script\">\n";
		print "<input type=submit value=' �f���ɖ߂� '></form>\n";
		print "</body>\n</html>\n";
		exit;
	}

	$com =~ s/<br>/\r/g;

	&header;
	print "[<a href=\"javascript:history.back()\">�߂�</a>]\n";
	print "<p>- �ύX���镔���̂ݏC�����đ��M�{�^���������ĉ����� -<br>\n";
	&form("edit",$no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color);
	print "</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �t�H�[�����̓`�F�b�N
#-------------------------------------------------
sub form_check {
	# ���T�C�g����̃A�N�Z�X��r��
	if ($base_url) {
		$baseUrl =~ s/(\W)/\\$1/g;

		$ref = $ENV{'HTTP_REFERER'};
		$ref =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		if ($ref && $ref !~ /$base_url/i) { &error("�s���ȃA�N�Z�X�ł�"); }
	}
	
	if ($in{'comment'} !~ m/[\x80-\x9f\xe0-\xfc]/) { &error("���{�ꂪ�܂܂�Ă��܂���"); }
	
	# method�v���p�e�B��POST����
	if ($ENV{'REQUEST_METHOD'} ne 'POST') { &error("�s���ȓ��e�ł�"); }

	# ���͍��ڂ̃`�F�b�N
	if ($in{'name'} eq "") { &error("���O�����͂���Ă��܂���"); }
	if ($in{'comment'} eq "") { &error("�R�����g�����͂���Ă��܂���"); }
	if ($in_email) {
		if ($in{'email'} eq "") { &error("�d���[�������͂���Ă��܂���"); }
		elsif ($in{'email'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,6}$/) {
			&error("�d���[���̓��͓��e���s���ł�");
		}
	}
}

#-------------------------------------------------
#  ���Ԃ��擾
#-------------------------------------------------
sub get_time {
	$ENV{'TZ'} = "JST-9";
	$times = time;
	($min,$hour,$mday,$mon,$year,$wday) = (localtime($times))[1..6];
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# �����̃t�H�[�}�b�g
	$date = sprintf("%04d/%02d/%02d(%s) %02d:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min);
}

#-------------------------------------------------
#  �J�E���^����
#-------------------------------------------------
sub counter {
	local($count, $cntup, @count);

	# �{�����̂݃J�E���g�A�b�v
	if ($mode eq '' or $mode eq 'thview' or $mode eq 'list' or $mode eq 'past') { $cntup = 1; } else { $cntup = 0; }

	# �J�E���g�t�@�C����ǂ݂���
	open(LOG,"+< $cntfile") || &error("Open Error: $cntfile");
	eval "flock(LOG, 2);";
	$count = <LOG>;

	# IP�`�F�b�N�ƃ��O�j���`�F�b�N
	local($cnt, $ip) = split(/:/, $count);
#	if ($addr eq $ip || $cnt eq "") { $cntup = 0; }

	# �J�E���g�A�b�v
	if ($cntup) {
		$cnt++;
		truncate(LOG, 0);
		seek(LOG, 0, 0);
		print LOG "$cnt:dummy";
	}
	close(LOG);

	# ��������
	while(length($cnt) < $mini_fig) { $cnt = '0' . $cnt; }
	@cnts = split(//, $cnt);

	# GIF�J�E���^�\��
	if ($counter == 2) {
		foreach (0 .. $#cnts) {
			print "<img src=\"$gif_path$cnts[$_]\.gif\" alt=\"$cnts[$_]\" width=\"$mini_w\" height=\"$mini_h\">";
		}
	}
	# �e�L�X�g�J�E���^�\��
	else {
		print "<font color=\"$cnt_color\" face=\"verdana,Times New Roman,Arial\">$cnt</font><br>\n";
	}
}

#-------------------------------------------------
#  ���b�N����
#-------------------------------------------------
sub lock {
	# �Â����b�N�͍폜����
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}

	local($retry) = 5;

	# symlink�֐������b�N
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}

	# mkdir�֐������b�N
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag=1;
}

#-------------------------------------------------
#  ���b�N����
#-------------------------------------------------
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }
	$lockflag=0;
}

#-------------------------------------------------
#  ���[�����M
#-------------------------------------------------
sub mail_to {
	local($mcom,$hp,$msub,$mbody);

	# ���[���^�C�g�����`
	$msub = &base64("[$title : $no] $in{'sub'}");

	# �L���𕜌�
	$mcom  = $in{'comment'};
	$mcom =~ s/<br>/\n/g;
	$mcom =~ s/&lt;/</g;
	$mcom =~ s/&gt;/>/g;
	$mcom =~ s/&quot;/"/g;
	$mcom =~ s/&amp;/&/g;

	# URL���
	if ($in{'url'}) { $hp = "http://$in{'url'}"; }
	else { $hp = ""; }

	# ���[���{�����`
	$mbody = <<EOM;
���e�����F$date
�z�X�g���F$host
�u���E�U�F$ENV{'HTTP_USER_AGENT'}

���e�Җ��F$in{'name'}
�d���[���F$in{'email'}
�t�q�k  �F$hp
�^�C�g���F$in{'sub'}

$mcom
EOM

	# ���[���A�h���X���Ȃ��ꍇ�͊Ǘ��҃��[���ɒu������
	if ($in{'email'} eq "") { $email = $mailto; }
	else { $email = $in{'email'}; }

	open(MAIL,"| $sendmail -t -i") || &error("���M���s");
	print MAIL "To: $mailto\n";
	print MAIL "From: $email\n";
	print MAIL "Subject: $msub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	foreach ( split(/\n/, $mbody) ) {
		&jcode'convert(*_, 'jis', 'sjis');
		print MAIL $_, "\n";
	}
	close(MAIL);
}

#-------------------------------------------------
#  BASE64�ϊ�
#-------------------------------------------------
#	�Ƃقق�WWW����Ō��J����Ă��郋�[�`����
#	�Q�l�ɂ��܂����B( http://www.tohoho-web.com/ )
sub base64 {
	local($sub) = @_;
	&jcode'convert(*sub, 'jis', 'sjis');

	$sub =~ s/\x1b\x28\x42/\x1b\x28\x4a/g;
	$sub = "=?iso-2022-jp?B?" . &b64enc($sub) . "?=";
	$sub;
}
sub b64enc {
	local($ch)="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	local($x, $y, $z, $i);
	$x = unpack("B*", $_[0]);
	for ($i=0; $y=substr($x,$i,6); $i+=6) {
		$z .= substr($ch, ord(pack("B*", "00" . $y)), 1);
		if (length($y) == 2) {
			$z .= "==";
		} elsif (length($y) == 4) {
			$z .= "=";
		}
	}
	$z;
}

#-------------------------------------------------
#  �p�X���[�h�Í�����
#-------------------------------------------------
sub encrypt {
	local($inpw) = $_[0];
	local(@SALT, $salt, $encrypt);

	@SALT = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
	srand;
	$salt = $SALT[int(rand(@SALT))] . $SALT[int(rand(@SALT))];
	$encrypt = crypt($inpw, $salt) || crypt ($inpw, '$1$' . $salt);
	return $encrypt;
}

#-------------------------------------------------
#  �p�X���[�h�ƍ�����
#-------------------------------------------------
sub decrypt {
	local($inpw, $logpw) = @_;
	local($salt, $check);

	$salt = $logpw =~ /^\$1\$(.*)\$/ && $1 || substr($logpw, 0, 2);
	$check = "no";
	if (crypt($inpw, $salt) eq $logpw || crypt($inpw, '$1$' . $salt) eq $logpw)
		{ $check = "yes"; }
	return $check;
}

#-------------------------------------------------
#  HTML�w�b�_�[
#-------------------------------------------------
sub header {
	$headflag=1;
	print "Content-type: text/html\n\n";
	print <<"EOM";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<meta name="robots" content="noarchive">
<STYLE type="text/css">
<!--
body,td,th { font-size:$b_size; font-family:$face }
a:hover { color: $al }
-->
</STYLE>
<title>$title</title></head>
EOM

	if ($bg) {
		print "<body background=\"$bg\" bgcolor=\"$bc\" text=\"$tx\" link=\"$lk\" vlink=\"$vl\" alink=\"$al\">\n";
	} else {
		print "<body bgcolor=\"$bc\" text=\"$tx\" link=\"$lk\" vlink=\"$vl\" alink=\"$al\">\n";
	}
}

#-------------------------------------------------
#  ����URL�����N
#-------------------------------------------------
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(ttp\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"h$2\" target='_blank'>$2<\/a>/g;
	$_[0] =~ s/([^=^\"]|^)(ttps\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"h$2\" target='_blank'>$2<\/a>/g;
}

#-------------------------------------------------
#  �ߋ����O����
#-------------------------------------------------
sub pastlog {
	local($past_flag)=0;

	# �ߋ�NO���J��
	open(NO,"$nofile") || &error("Open Error : $nofile");
	$count = <NO>;
	close(NO);

	# �ߋ����O�̃t�@�C�������`
	$pastfile  = "$pastdir$count\.dat";

	# �ߋ����O���J��
	open(IN,"$pastfile") || open(IN,"+>$pastfile")  || &error("Open Error : $pastfile");
	@past = <IN>;
	close(IN);

	# �K��̍s�����I�[�o�[����Ǝ��t�@�C������������
	if ($#past > $log_line) {
		$past_flag=1;

		# �J�E���g�t�@�C���X�V
		$count++;
		open(NO,">$nofile") || &error("Write Error : $nofile");
		print NO $count;
		close(NO);

		$pastfile = "$pastdir$count\.dat";
		@past=();
	}

	@temp=();
	foreach (@data) {
		($pno,$preno,$pdate,$pname,$pmail,$psub,$pcom,$purl,$pho)
								 = split(/<>/);
		if ($pmail) { $pname = "<a href=\"mailto:$pmail\">$pname</a>"; }
		if ($purl) { $purl = "&lt;<a href=\"http://$purl\" target='_top'>HOME</a>&gt;"; }
		if ($preno) { $pno = "Res: $preno"; }

		# �ۑ��L�����t�H�[�}�b�g
		push(@temp,"<hr>[<b>$pno</b>] <font color=\"$sub_color\"><b>$psub</b></font> ���e�ҁF<b>$pname</b> ���e���F$pdate $purl<br><blockquote>$pcom</blockquote>\n");
	}

	# �ߋ����O���X�V
	unshift(@past,@temp);
	open(OUT,">$pastfile") || &error("Write Error : $pastfile");
	print OUT @past;
	close(OUT);

	if ($past_flag) { chmod(0666,$pastfile); }
}

#-------------------------------------------------
#  �ߋ����O
#-------------------------------------------------
sub past {
	open(IN,"$nofile") || &error("Open Error : $nofile");
	$pastno = <IN>;
	close(IN);

	if (!$in{'pastlog'}) { $in{'pastlog'} = $pastno; }

	&header;

	# �J�E���^����
	if ($counter) { &counter; }

	print <<"EOM";
<BR>
[<a href="$script?">�f���ɖ߂�</a>]
<table width="100%"><tr><th bgcolor="#880000">
  <font color="#FFFFFF">�ߋ����O[$in{'pastlog'}]</font>
</th></tr></table>
<p><table border=0><tr><td>
<form action="$script" method="POST">
<input type=hidden name=mode value=past>
�ߋ����O�F<select name=pastlog>
EOM

	$pastkey = $pastno;
	while ($pastkey > 0) {
		if ($in{'pastlog'} == $pastkey) {
			print "<option value=\"$pastkey\" selected>$pastkey Page\n";
		} else {
			print "<option value=\"$pastkey\">$pastkey Page\n";
		}
		$pastkey--;
	}
	print "</select>\n<input type=submit value='�ړ�'></td></form>\n";
	print "<td width=30></td><td>\n";
	print "<form action=\"$script\" method=\"POST\">\n";
	print "<input type=hidden name=mode value=past>\n";
	print "<input type=hidden name=pastlog value=\"$in{'pastlog'}\">\n";
	print "���[�h�����F<input type=text name=word size=30 value=\"$in{'word'}\">\n";
	print "�����F<select name=cond>\n";

	foreach ('AND', 'OR') {
		if ($in{'cond'} eq "$_") {
			print "<option value=\"$_\" selected>$_\n";
		} else {
			print "<option value=\"$_\">$_\n";
		}
	}
	print "</select>\n";
	print "�\\���F<select name=view>\n";
	if ($in{'view'} eq "") { $in{'view'} = $p_log; }
	foreach (5,10,15,20,25,30) {
		if ($in{'view'} eq "$_") {
			print "<option value=\"$_\" selected>$_��\n";
		} else {
			print "<option value=\"$_\">$_��\n";
		}
	}
	print "</select>\n<input type=submit value='����'></td></form>\n";
	print "</tr></table>\n";

	# �\�����O���`
	$in{'pastlog'} =~ s/\D//g;
	$file = "$pastdir$in{'pastlog'}\.dat";

	# ���[�h��������
	if ($in{'word'} ne "") {
		$in{'word'} =~ s/�@/ /g;
		@pairs = split(/\s+/, $in{'word'});

		@new=();
		open(IN,"$file") || &error("Open Error : $file");
		while (<IN>) {
			$flag=0;
			foreach $pair (@pairs) {
				if (index($_,$pair) >= 0) {
					$flag=1;
					if ($in{'cond'} eq 'OR') { last; }
				} else {
					if ($in{'cond'} eq 'AND') { $flag=0; last; }
				}
			}
			if ($flag) { push(@new,$_); }
		}
		close(IN);

		$count = @new;
		print "�������ʁF<b>$count</b>��\n";
		if ($page eq '') { $page = 0; }
		$end_data = @new - 1;
		$page_end = $page + $in{'view'} - 1;
		if ($page_end >= $end_data) { $page_end = $end_data; }

		$next_line = $page_end + 1;
		$back_line = $page - $in{'view'};

		$enwd = &url_enc($in{'word'});
		if ($back_line >= 0) {
			print "[<a href=\"$script?mode=past&page=$back_line&word=$enwd&view=$in{'view'}&cond=$in{'cond'}&pastlog=$in{'pastlog'}\">�O��$in{'view'}��</a>]\n";
		}
		if ($page_end ne "$end_data") {
			print "[<a href=\"$script?mode=past&page=$next_line&word=$enwd&view=$in{'view'}&cond=$in{'cond'}&pastlog=$in{'pastlog'}\">����$in{'view'}��</a>]\n";
		}
		# �\���J�n
		foreach ($page .. $page_end) { print $new[$_]; }
		print "<hr>\n</body></html>\n";
		exit;
	}

	# �y�[�W��؂菈��
	$start = $page + 1;
	$end   = $page + $p_log;

	$i=0;
	open(IN,"$file") || &error("Open Error : $file");
	while (<IN>) {
		$flag=0;
		if ($_ =~ /^\<hr\>\[\<b\>\d+\<\/b\>\]/) { $flag=1; $i++; }
		if ($i < $start) { next; }
		if ($i > $end) { last; }

		if ($flag) { print $_; }
		else {
			$_ =~ s/<hr>//ig;
			print "<blockquote>$_</blockquote>\n";
		}
	}
	close(IN);
	print "<hr>\n";

	$next = $page + $p_log;
	$back = $page - $p_log;
	print "<table>\n";
	if ($back >= 0) {
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=past>\n";
		print "<input type=hidden name=pastlog value=\"$in{'pastlog'}\">\n";
		print "<input type=hidden name=page value=\"$back\">\n";
		print "<input type=submit value=\"�O��$p_log��\"></td></form>\n";
	}
	if ($next < $i) {
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=past>\n";
		print "<input type=hidden name=pastlog value=\"$in{'pastlog'}\">\n";
		print "<input type=hidden name=page value=\"$next\">\n";
		print "<input type=submit value=\"����$p_log��\"></td></form>\n";
	}
	print "</table>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �`�F�b�N���[�h
#-------------------------------------------------
sub check {
	&header;
	print "<h2>Check Mode</h2>\n";
	print "<ul>\n";

	# ���O�p�X
	if (-e $logfile) {
		print "<li>���O�t�@�C���̃p�X�FOK\n";
		# �p�[�~�b�V����
		if (-r $logfile && -w $logfile) {
			print "<li>���O�t�@�C���̃p�[�~�b�V�����FOK\n";
		} else { print "<li>���O�t�@�C���̃p�[�~�b�V�����FNG\n"; }
	} else { print "<li>���O�t�@�C���̃p�X�FNG �� $logfile\n"; }

	# �J�E���^���O
	print "<li>�J�E���^�F";
	if ($counter) {
		print "�ݒ肠��\n";
		if (-e $cntfile) { print "<li>�J�E���^���O�t�@�C���̃p�X�FOK\n"; }
		else { print "<li>�J�E���^���O�t�@�C���̃p�X�FNG �� $cntfile\n"; }
	} else { print "�ݒ�Ȃ�\n"; }

	# ���b�N�f�B���N�g��
	print "<li>���b�N�`���F";
	if ($lockkey == 0) { print "���b�N�ݒ�Ȃ�\n"; }
	else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }
		($lockdir) = $lockfile =~ /(.*)[\\\/].*$/;
		print "<li>���b�N�f�B���N�g���F$lockdir\n";

		if (-d $lockdir) {
			print "<li>���b�N�f�B���N�g���̃p�X�FOK\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<li>���b�N�f�B���N�g���̃p�[�~�b�V�����FOK\n";
			} else {
				print "<li>���b�N�f�B���N�g���̃p�[�~�b�V�����FNG �� $lockdir\n";
			}
		} else { print "<li>���b�N�f�B���N�g���̃p�X�FNG �� $lockdir\n"; }
	}

	# �摜�f�B���N�g��
	print "<li>�摜�f�B���N�g���F$imgdir\n";
	if (-d $imgdir) {
		print "<li>�摜�f�B���N�g���̃p�X�FOK\n";
		if (-r $imgdir && -w $imgdir && -x $imgdir) {
			print "<li>�摜�f�B���N�g���̃p�[�~�b�V�����FOK\n";
		} else {
			print "<li>�摜�f�B���N�g���̃p�[�~�b�V�����FNG �� $imgdir\n";
		}
	} else { print "<li>�摜�f�B���N�g���FNG �� $imgdir\n"; }

	# �ߋ����O
	print "<li>�ߋ����O�F";
	if ($pastkey == 0) { print "�ݒ�Ȃ�\n"; }
	else {
		print "�ݒ肠��\n";

		# NO�t�@�C��
		if (-e $nofile) {
			print "<li>NO�t�@�C���p�X�FOK\n";
			if (-r $nofile && -w $nofile) {
				print "<li>NO�t�@�C���p�[�~�b�V�����FOK\n";
			} else { print "<li>NO�t�@�C���p�[�~�b�V�����FNG �� $nofile\n"; }
		} else { print "<li>NO�t�@�C���̃p�X�FNG �� $nofile\n"; }

		# �f�B���N�g��
		if (-d $pastdir) {
			print "<li>�ߋ����O�f�B���N�g���p�X�FOK\n";
			if (-r $pastdir && -w $pastdir && -x $pastdir) {
				print "<li>�ߋ����O�f�B���N�g���p�[�~�b�V�����FOK\n";
			} else {
				print "<li>�ߋ����O�f�B���N�g���p�[�~�b�V�����FNG �� $pastdir\n";
			}
		} else { print "<li>�ߋ����O�f�B���N�g���p�[�~�b�V�����FNG �� $pastdir\n"; }
	}
	print "</ul>\n</body></html>\n";
	exit;
}

#-------------------------------------------------
#  JPEG�T�C�Y�F��
#-------------------------------------------------
sub JpegSize {
	local($jpeg) = @_;
	local($t, $m, $c, $l, $W, $H);

	open(JPEG,"$jpeg") || return (0,0);
	binmode JPEG;
	read(JPEG, $t, 2);
	while (1) {
		read(JPEG, $t, 4);
		($m, $c, $l) = unpack("a a n", $t);

		if ($m ne "\xFF") { $W = $MaxW; $H = $MaxH; last; }
		elsif ((ord($c) >= 0xC0) && (ord($c) <= 0xC3)) {
			read(JPEG, $t, 5);
			($H, $W) = unpack("xnn", $t);
			last;
		}
		else {
			read(JPEG, $t, ($l - 2));
		}
	}
	close(JPEG);
	return ($W, $H);
}

#-------------------------------------------------
#  GIF�T�C�Y�F��
#-------------------------------------------------
sub GifSize {
	local($gif) = @_;
	local($data);

	open(GIF,"$gif") || return (0,0);
	binmode(GIF);
	sysread(GIF,$data,10);
	close(GIF);

	if ($data =~ /^GIF/) { $data = substr($data,-4); }

	$W = unpack("v",substr($data,0,2));
	$H = unpack("v",substr($data,2,2));
	return ($W, $H);
}

#-------------------------------------------------
#  PNG�T�C�Y�F��
#-------------------------------------------------
sub PngSize {
	local($png) = @_;
	local($data);

	open(PNG, "$png") || return (0,0);
	binmode(PNG);
	read(PNG, $data, 24);
	close(PNG);

	$W = unpack("N", substr($data, 16, 20));
	$H = unpack("N", substr($data, 20, 24));
	return ($W, $H);
}

#-------------------------------------------------
#  URL�G���R�[�h
#-------------------------------------------------
sub url_enc {
	local($_) = @_;

	s/(\W)/'%' . unpack('H2', $1)/eg;
	s/\s/+/g;
	$_;
}

#-------------------------------------------------
#  ���e�t�H�[��
#-------------------------------------------------
sub form {
	local($type,$no,$reno,$date,$name,$mail,$sub,$com,$url,$host,$pw,$color) = @_;
	local($cnam,$ceml,$curl,$cpwd,$cico,$ccol);

	print "<blockquote>\n";

	## �t�H�[����ʂ𔻕�
	# �C��
	if ($type eq "edit") {
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"usr_edt\">\n";
		print "<input type=hidden name=action value=\"edit\">\n";
		print "<input type=hidden name=pwd value=\"$in{'pwd'}\">\n";
		print "<input type=hidden name=no value=\"$in{'no'}\">\n";
		$cnam = $name;
		$ceml = $mail;
		$curl = $url;
		$ccol = $color;
	# �ԐM
	} elsif ($type eq "res") {
		if ($res_clip) {
			print "<form action=\"$script\" method=\"POST\" enctype=\"multipart/form-data\">\n";
		} else {
			print "<form action=\"$script\" method=\"POST\">\n";
		}
		print "<input type=hidden name=mode value=\"regist\">\n";
		print "<input type=hidden name=reno value=\"$in{'no'}\">\n";
		($cnam,$ceml,$curl,$cpwd,$cico,$ccol) = &get_cookie;
	# �V�K
	} else {
		print "<form action=\"$script\" method=\"POST\" enctype=\"multipart/form-data\">\n";
		print "<input type=hidden name=mode value=\"regist\">\n";
		($cnam,$ceml,$curl,$cpwd,$cico,$ccol) = &get_cookie;
	}

	print <<"EOM";
<table border=0 cellspacing=0>
<tr>
  <td nowrap><b>���Ȃ܂�</b></td>
  <td><input type=text name=name size=28 value="$cnam"></td>
</tr>
<tr>
  <td nowrap><b>�d���[��</b></td>
  <td><input type=text name=email size=28 value="$ceml"></td>
</tr>
<tr>
  <td nowrap><b>�^�C�g��</b></td>
  <td nowrap>
    <input type=text name=sub size=36 value="$sub">
<input type=submit value="���e����"><input type=reset value="���Z�b�g">
  </td>
</tr>
<tr>
  <td colspan=2>
    <b>�R�����g</b><br>
    <textarea cols=80 rows=14 name=comment wrap="soft">$com</textarea>
  </td>
</tr>
<tr>
  <td nowrap><b>�t�q�k</b></td>
  <td><input type=text size=50 name=url value="http://$curl"></td>
</tr>
EOM
	# �Y�t�t�H�[��
	if ($type eq "" || ($type eq "res" && $res_clip)) {
		print "<tr><td><b>�Y�tFile</b></td>\n";
		print "<td><input type=file name=upfile size=40></td></tr>\n";
	}
	# �p�X���[�h��
	if ($type ne "edit") {
		print "<tr><td nowrap><b>�Ï؃L�[</b></td>";
		print "<td><input type=password name=pwd size=8 maxlength=8 value=\"$cpwd\"> ";
		print "(�p������8�����ȓ�)</td></tr>\n";
	}

	# �F�w��
	print "<tr><td nowrap><b>�����F</b></td><td>\n";
	@col = split(/\s+/, $colors);
	if ($ccol eq "") { $ccol = $col[0]; }
	foreach (@col) {
		if ($ccol eq $_) {
			print "<input type=radio name=color value=\"$_\" checked><font color=\"$_\">��</font>\n";
		} else {
			print "<input type=radio name=color value=\"$_\"><font color=\"$_\">��</font>\n";
		}
	}
	print "</td></tr></table></form>\n";
	if ($ImageCheck) {
		print "�E�摜�͊Ǘ��҂�������܂ŁuCOMING SOON�v�̃A�C�R�����\\������܂��B<br>\n";
	}
	print "</blockquote>\n";
}

#-------------------------------------------------
#  �֎~���[�h
#-------------------------------------------------
sub deny_word {
	local($word) = @_;

	local($flg);
	foreach ( split(/,+/, $deny_word) ) {
		if (index($word,$_) >= 0) { $flg=1; last; }
	}
	if ($flg) { &error("�֎~���(http://��)���܂܂�Ă��邽�ߎ󗝂ł��܂���B�ڍׂ͂��₢���킹������<BR>"); }
}

sub send_mail {
	my $send_mail	= '/usr/sbin/sendmail';
	my $from	= $_[0]; 
	my $to		= $_[1];
	my $cc		= $_[2];
	my $subject	= $_[3];
	my $msg		= $_[4];
	
	&jcode::convert(\$subject,'jis');
	&jcode::convert(\$msg,'jis');
	
	# sendmail �R�}���h�N��
	open(SDML,"| $send_mail -t -i") || die 'sendmail error';
	# ���[���w�b�_�o��
	print SDML "From: $from\n";
	print SDML "To: $to\n";
	print SDML "Cc: $cc\n";
	print SDML "Subject: $subject\n";
	print SDML "Content-Transfer-Encoding: 7bit\n";
	print SDML "Content-type: text/plain;charset=\"ISO-2022-JP\"\n\n"; 
	# ���[���{���o��
	print SDML "$msg\n";
	# sendmail �R�}���h����
	close(SDML); 
}

__END__

