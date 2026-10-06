FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2026-10-04-git-a35c879992-essentials_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/a35c879992

git-essentials build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
CLMUL enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
6 registers available     yes
7 registers available     yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
experimental features     yes
xmllint enabled           yes

External libraries:
avisynth                libmp3lame              libvorbis
bzlib                   libopencore_amrnb       libvpx
cairo                   libopencore_amrwb       libwebp
gmp                     libopenjpeg             libx264
gnutls                  libopenmpt              libx265
iconv                   libopus                 libxml2
libaom                  librubberband           libxvid
libass                  libspeex                libzimg
libfontconfig           libsrt                  libzmq
libfreetype             libssh                  lzma
libfribidi              libtheora               mediafoundation
libgme                  libvidstab              openal
libgsm                  libvmaf                 sdl2
libharfbuzz             libvo_amrwbenc          zlib

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               vaapi
cuvid                   libmfx
d3d11va                 libvpl

Libraries:
avcodec                 avformat                swscale
avdevice                avutil
avfilter                swresample

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     fits                    pcm_u8
aac_fixed               flac                    pcm_vidc
aac_latm                flashsv                 pcx
aasc                    flashsv2                pdv
ac3                     flic                    pfm
ac3_fixed               flv                     pgm
acelp_kelvin            fmvc                    pgmyuv
adpcm_4xm               fourxm                  pgssub
adpcm_adx               fraps                   pgx
adpcm_afc               frwu                    phm
adpcm_agm               ftr                     photocd
adpcm_aica              g2m                     pictor
adpcm_argo              g723_1                  pixlet
adpcm_circus            g728                    pjs
adpcm_ct                g729                    png
adpcm_dtk               gdv                     ppm
adpcm_ea                gem                     prores
adpcm_ea_maxis_xa       gif                     prores_raw
adpcm_ea_r1             gremlin_dpcm            prosumer
adpcm_ea_r2             gsm                     psd
adpcm_ea_r3             gsm_ms                  ptx
adpcm_ea_xas            h261                    qcelp
adpcm_g722              h263                    qdm2
adpcm_g726              h263i                   qdmc
adpcm_g726le            h263p                   qdraw
adpcm_ima_acorn         h264                    qoa
adpcm_ima_alp           h264_amf                qoi
adpcm_ima_amv           h264_cuvid              qpeg
adpcm_ima_apc           h264_qsv                qtrle
adpcm_ima_apm           hap                     r10k
adpcm_ima_citrix        hca                     r210
adpcm_ima_cunning       hcom                    ra_144
adpcm_ima_dat4          hdr                     ra_288
adpcm_ima_dk3           hevc                    ralf
adpcm_ima_dk4           hevc_amf                rasc
adpcm_ima_ea_eacs       hevc_cuvid              rawvideo
adpcm_ima_ea_sead       hevc_qsv                realtext
adpcm_ima_escape        hnm4_video              rka
adpcm_ima_hvqm2         hq_hqa                  rl2
adpcm_ima_hvqm4         hqx                     roq
adpcm_ima_iss           huffyuv                 roq_dpcm
adpcm_ima_magix         hymt                    rpza
adpcm_ima_moflex        iac                     rscc
adpcm_ima_mtf           idcin                   rtv1
adpcm_ima_oki           idf                     rv10
adpcm_ima_pda           iff_ilbm                rv20
adpcm_ima_qt            ilbc                    rv30
adpcm_ima_rad           imc                     rv40
adpcm_ima_smjpeg        imm4                    rv60
adpcm_ima_ssi           imm5                    s302m
adpcm_ima_wav           indeo2                  sami
adpcm_ima_ws            indeo3                  sanm
adpcm_ima_xbox          indeo4                  sbc
adpcm_ms                indeo5                  scpr
adpcm_mtaf              interplay_acm           screenpresso
adpcm_n64               interplay_dpcm          sdx2_dpcm
adpcm_psx               interplay_video         sga
adpcm_psxc              ipu                     sgi
adpcm_rhetorex          jacosub                 sgirle
adpcm_sanyo             jpeg2000                sheervideo
adpcm_sbpro_2           jpegls                  shorten
adpcm_sbpro_3           jv                      simbiosis_imx
adpcm_sbpro_4           kgv1                    sipr
adpcm_swf               kmvc                    siren
adpcm_thp               lagarith                smackaud
adpcm_thp_le            lead                    smacker
adpcm_vima              libaom_av1              smc
adpcm_xa                libgsm                  smvjpeg
adpcm_xmd               libgsm_ms               snow
adpcm_yamaha            libopencore_amrnb       sol_dpcm
adpcm_zork              libopencore_amrwb       sp5x
agm                     libopus                 speedhq
ahx                     libspeex                speex
aic                     libvorbis               srgc
alac                    libvpx_vp8              srt
alias_pix               libvpx_vp9              ssa
als                     loco                    stl
amrnb                   lscr                    subrip
amrwb                   m101                    subviewer
amv                     mace3                   subviewer1
anm                     mace6                   sunrast
ansi                    magicyuv                svq1
anull                   mdec                    svq3
apac                    media100                tak
ape                     metasound               targa
apng                    microdvd                targa_y216
aptx                    mimic                   tdsc
aptx_hd                 misc4                   text
apv                     mjpeg                   theora
arbc                    mjpeg_cuvid             thp
argo                    mjpeg_qsv               tiertexseqvideo
ass                     mjpegb                  tiff
asv1                    mlp                     tmv
asv2                    mmvideo                 truehd
atrac1                  mobiclip                truemotion1
atrac3                  motionpixels            truemotion2
atrac3al                movtext                 truemotion2rt
atrac3p                 mp1                     truespeech
atrac3pal               mp1float                tscc
atrac9                  mp2                     tscc2
aura                    mp2float                tta
aura2                   mp3                     twinvq
av1                     mp3adu                  txd
av1_amf                 mp3adufloat             ulti
av1_cuvid               mp3float                utvideo
av1_qsv                 mp3on4                  v210
avrn                    mp3on4float             v210x
avrp                    mpc7                    vb
avs                     mpc8                    vble
avui                    mpeg1_cuvid             vbn
bethsoftvid             mpeg1video              vc1
bfi                     mpeg2_cuvid             vc1_cuvid
bink                    mpeg2_qsv               vc1_qsv
binkaudio_dct           mpeg2video              vc1image
binkaudio_rdft          mpeg4                   vcr1
bintext                 mpeg4_cuvid             vmdaudio
bitpacked               mpegvideo               vmdvideo
bmp                     mpl2                    vmix
bmv_audio               msa1                    vmnc
bmv_video               mscc                    vnull
bonk                    msmpeg4v1               vorbis
brender_pix             msmpeg4v2               vp3
c93                     msmpeg4v3               vp4
cavs                    msnsiren                vp5
cbd2_dpcm               msp2                    vp6
ccaption                msrle                   vp6a
cdgraphics              mss1                    vp6f
cdtoons                 mss2                    vp7
cdxl                    msvideo1                vp8
cfhd                    mszh                    vp8_cuvid
cinepak                 mts2                    vp8_qsv
clearvideo              mv30                    vp9
cljr                    mvc1                    vp9_amf
cllc                    mvc2                    vp9_cuvid
comfortnoise            mvdv                    vp9_qsv
cook                    mvha                    vplayer
cpia                    mwsc                    vqa
cri                     mxpeg                   vqc
cscd                    nellymoser              vvc
cyuv                    notchlc                 vvc_qsv
dca                     nuv                     wady_dpcm
dds                     on2avc                  wavarc
derf_dpcm               opus                    wavpack
dfa                     osq                     wbmp
dfpwm                   paf_audio               wcmv
dirac                   paf_video               webp
dnxhd                   pam                     webp_anim
dolby_e                 pbm                     webvtt
dpx                     pcm_alaw                wmalossless
dsd_lsbf                pcm_bluray              wmapro
dsd_lsbf_planar         pcm_dvd                 wmav1
dsd_msbf                pcm_dvda                wmav2
dsd_msbf_planar         pcm_f16le               wmavoice
dsicinaudio             pcm_f24le               wmv1
dsicinvideo             pcm_f32be               wmv2
dss_sp                  pcm_f32le               wmv3
dst                     pcm_f64be               wmv3image
dvaudio                 pcm_f64le               wnv1
dvbsub                  pcm_lxf                 wrapped_avframe
dvdsub                  pcm_mulaw               ws_snd1
dvvideo                 pcm_s16be               xan_dpcm
dxa                     pcm_s16be_planar        xan_wc3
dxtory                  pcm_s16le               xan_wc4
dxv                     pcm_s16le_planar        xbin
eac3                    pcm_s24be               xbm
eacmv                   pcm_s24daud             xface
eamad                   pcm_s24le               xl
eatgq                   pcm_s24le_planar        xma1
eatgv                   pcm_s32be               xma2
eatqi                   pcm_s32le               xpm
eightbps                pcm_s32le_planar        xsub
eightsvx_exp            pcm_s64be               xwd
eightsvx_fib            pcm_s64le               y41p
escape124               pcm_s8                  ylc
escape130               pcm_s8_planar           yop
evrc                    pcm_sga                 yuv4
exr                     pcm_u16be               zero12v
fastaudio               pcm_u16le               zerocodec
ffv1                    pcm_u24be               zlib
ffvhuff                 pcm_u24le               zmbv
ffwavesynth             pcm_u32be
fic                     pcm_u32le

Enabled encoders:
a64multi                h264_vaapi              pcm_s8
a64multi5               hdr                     pcm_s8_planar
aac                     hevc_amf                pcm_u16be
aac_mf                  hevc_d3d12va            pcm_u16le
ac3                     hevc_mf                 pcm_u24be
ac3_fixed               hevc_nvenc              pcm_u24le
ac3_mf                  hevc_qsv                pcm_u32be
adpcm_adx               hevc_vaapi              pcm_u32le
adpcm_argo              huffyuv                 pcm_u8
adpcm_g722              jpeg2000                pcm_vidc
adpcm_g726              jpegls                  pcx
adpcm_g726le            libaom_av1              pdv
adpcm_ima_alp           libgsm                  pfm
adpcm_ima_amv           libgsm_ms               pgm
adpcm_ima_apm           libmp3lame              pgmyuv
adpcm_ima_qt            libopencore_amrnb       phm
adpcm_ima_ssi           libopenjpeg             png
adpcm_ima_wav           libopus                 ppm
adpcm_ima_ws            libspeex                prores
adpcm_ms                libtheora               prores_aw
adpcm_swf               libvo_amrwbenc          prores_ks
adpcm_yamaha            libvorbis               qoi
alac                    libvpx_vp8              qtrle
alias_pix               libvpx_vp9              r10k
amv                     libwebp                 r210
anull                   libwebp_anim            ra_144
apng                    libx264                 rawvideo
aptx                    libx264rgb              roq
aptx_hd                 libx265                 roq_dpcm
ass                     libxvid                 rpza
asv1                    ljpeg                   rv10
asv2                    magicyuv                rv20
av1_amf                 mjpeg                   s302m
av1_d3d12va             mjpeg_qsv               sbc
av1_mf                  mjpeg_vaapi             sgi
av1_nvenc               mlp                     smc
av1_qsv                 movtext                 snow
av1_vaapi               mp2                     speedhq
avrp                    mp2fixed                srt
avui                    mp3_mf                  ssa
bitpacked               mpeg1video              subrip
bmp                     mpeg2_qsv               sunrast
cfhd                    mpeg2_vaapi             svq1
cinepak                 mpeg2video              targa
cljr                    mpeg4                   text
comfortnoise            msmpeg4v2               tiff
dca                     msmpeg4v3               truehd
dfpwm                   msrle                   tta
dnxhd                   msvideo1                ttml
dpx                     nellymoser              utvideo
dsd_msbf                opus                    v210
dvbsub                  pam                     vbn
dvdsub                  pbm                     vc2
dvvideo                 pcm_alaw                vnull
dxv                     pcm_bluray              vorbis
eac3                    pcm_dvd                 vp8_vaapi
exr                     pcm_f32be               vp9_qsv
ffv1                    pcm_f32le               vp9_vaapi
ffvhuff                 pcm_f64be               wavpack
fits                    pcm_f64le               wbmp
flac                    pcm_mulaw               webvtt
flashsv                 pcm_s16be               wmav1
flashsv2                pcm_s16be_planar        wmav2
flv                     pcm_s16le               wmv1
g723_1                  pcm_s16le_planar        wmv2
gif                     pcm_s24be               wrapped_avframe
h261                    pcm_s24daud             xbm
h263                    pcm_s24le               xface
h263p                   pcm_s24le_planar        xsub
h264_amf                pcm_s32be               xwd
h264_d3d12va            pcm_s32le               y41p
h264_mf                 pcm_s32le_planar        yuv4
h264_nvenc              pcm_s64be               zlib
h264_qsv                pcm_s64le               zmbv

Enabled hwaccels:
av1_d3d11va             hevc_vaapi              vc1_vaapi
av1_d3d11va2            mjpeg_nvdec             vp8_nvdec
av1_d3d12va             mjpeg_vaapi             vp8_nvdec_cuarray
av1_dxva2               mpeg1_nvdec             vp8_vaapi
av1_nvdec               mpeg1_nvdec_cuarray     vp9_d3d11va
av1_nvdec_cuarray       mpeg2_d3d11va           vp9_d3d11va2
av1_vaapi               mpeg2_d3d11va2          vp9_d3d12va
h263_vaapi              mpeg2_d3d12va           vp9_dxva2
h264_d3d11va            mpeg2_dxva2             vp9_nvdec
h264_d3d11va2           mpeg2_nvdec             vp9_nvdec_cuarray
h264_d3d12va            mpeg2_nvdec_cuarray     vp9_vaapi
h264_dxva2              mpeg2_vaapi             vvc_vaapi
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va
h264_nvdec_cuarray      mpeg4_nvdec_cuarray     wmv3_d3d11va2
h264_vaapi              mpeg4_vaapi             wmv3_d3d12va
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_d3d12va            vc1_d3d12va             wmv3_nvdec_cuarray
hevc_dxva2              vc1_dxva2               wmv3_vaapi
hevc_nvdec              vc1_nvdec
hevc_nvdec_cuarray      vc1_nvdec_cuarray

Enabled parsers:
aac                     dvdsub                  mpegaudio
aac_latm                evc                     mpegvideo
ac3                     ffv1                    opus
adx                     flac                    png
ahx                     ftr                     pnm
amr                     g723_1                  prores
apv                     g729                    prores_raw
av1                     gif                     qoi
avs2                    gsm                     rv34
avs3                    h261                    sbc
bmp                     h263                    sipr
cavsvideo               h264                    tak
cook                    hdr                     vc1
cri                     hevc                    vorbis
dca                     ipu                     vp3
dirac                   jpeg2000                vp8
dnxhd                   jpegxl                  vp9
dnxuc                   jpegxs                  vvc
dolby_e                 lcevc                   webp
dpx                     misc4                   xbm
dvaudio                 mjpeg                   xma
dvbsub                  mlp                     xwd
dvd_nav                 mpeg4video

Enabled demuxers:
aa                      idcin                   pcm_f64le
aac                     idf                     pcm_mulaw
aax                     iff                     pcm_s16be
ac3                     ifv                     pcm_s16le
ac4                     ilbc                    pcm_s24be
ace                     image2                  pcm_s24le
acm                     image2_alias_pix        pcm_s32be
act                     image2_brender_pix      pcm_s32le
adf                     image2pipe              pcm_s8
adp                     image_bmp_pipe          pcm_u16be
ads                     image_cri_pipe          pcm_u16le
adx                     image_dds_pipe          pcm_u24be
aea                     image_dpx_pipe          pcm_u24le
afc                     image_exr_pipe          pcm_u32be
aiff                    image_gem_pipe          pcm_u32le
aix                     image_gif_pipe          pcm_u8
alp                     image_hdr_pipe          pcm_vidc
amr                     image_j2k_pipe          pdv
amrnb                   image_jpeg_pipe         pjs
amrwb                   image_jpegls_pipe       pmp
anm                     image_jpegxl_pipe       pp_bnk
apac                    image_jpegxs_pipe       pva
apc                     image_pam_pipe          pvf
ape                     image_pbm_pipe          qcp
apm                     image_pcx_pipe          qoa
apng                    image_pfm_pipe          r3d
aptx                    image_pgm_pipe          rawvideo
aptx_hd                 image_pgmyuv_pipe       rcwt
apv                     image_pgx_pipe          realtext
aqtitle                 image_phm_pipe          redspark
argo_asf                image_photocd_pipe      rka
argo_brp                image_pictor_pipe       rl2
argo_cvg                image_png_pipe          rm
asf                     image_ppm_pipe          roq
asf_o                   image_psd_pipe          rpl
ass                     image_qdraw_pipe        rsd
ast                     image_qoi_pipe          rso
astc                    image_sgi_pipe          rtp
au                      image_sunrast_pipe      rtsp
av1                     image_svg_pipe          s337m
avi                     image_tiff_pipe         sami
avisynth                image_vbn_pipe          sap
avr                     image_webp_pipe         sbc
avs                     image_xbm_pipe          sbg
avs2                    image_xpm_pipe          scc
avs3                    image_xwd_pipe          scd
bethsoftvid             imf                     sdns
bfi                     ingenient               sdp
bfstm                   ipmovie                 sdr2
bink                    ipu                     sds
binka                   ircam                   sdx
bintext                 iss                     segafilm
bit                     iv8                     ser
bitpacked               ivf                     sga
bmv                     ivr                     shorten
boa                     jacosub                 siff
bonk                    jpegxl_anim             simbiosis_imx
brstm                   jv                      sln
c93                     ktx                     smacker
caf                     kux                     smjpeg
cavsvideo               kvag                    smush
cdg                     laf                     sol
cdxl                    lc3                     sox
cine                    libgme                  spdif
codec2                  libopenmpt              srt
codec2raw               live_flv                stl
concat                  lmlm4                   str
dash                    loas                    subviewer
data                    lrc                     subviewer1
daud                    luodat                  sup
dcstr                   lvf                     svag
derf                    lxf                     svs
dfa                     m4v                     swf
dfpwm                   matroska                tak
dhav                    mca                     tedcaptions
dirac                   mcc                     thp
dnxhd                   mgsts                   threedostr
dsf                     microdvd                tiertexseq
dsicin                  mjpeg                   tmv
dss                     mjpeg_2000              truehd
dts                     mlp                     tta
dtshd                   mlv                     tty
dv                      mm                      txd
dvbsub                  mmf                     ty
dvbtxt                  mods                    usm
dxa                     moflex                  v210
ea                      mov                     v210x
ea_cdata                mp3                     vag
eac3                    mpc                     vc1
epaf                    mpc8                    vc1t
evc                     mpegps                  vividas
ffmetadata              mpegts                  vivo
filmstrip               mpegtsraw               vmd
fits                    mpegvideo               vobsub
flac                    mpjpeg                  voc
flic                    mpl2                    vpk
flv                     mpsub                   vplayer
fourxm                  msf                     vqf
frm                     msnwc_tcp               vvc
fsb                     msp                     w64
fwse                    mtaf                    wady
g722                    mtv                     wav
g723_1                  musx                    wavarc
g726                    mv                      wc3
g726le                  mvi                     webm_dash_manifest
g728                    mvr                     webp_anim
g729                    mxf                     webvtt
gdv                     mxg                     wsaud
genh                    nc                      wsd
gif                     nistsphere              wsvqa
gsm                     nsp                     wtv
gxf                     nsv                     wv
h261                    nut                     wve
h263                    nuv                     xa
h264                    obu                     xbin
hca                     ogg                     xmd
hcom                    oma                     xmv
hevc                    osq                     xvag
hls                     paf                     xwma
hnm                     pcm_alaw                yop
hxvs                    pcm_f32be               yuv4mpegpipe
iamf                    pcm_f32le
ico                     pcm_f64be

Enabled muxers:
a64                     h264                    pcm_s16le
ac3                     hash                    pcm_s24be
ac4                     hds                     pcm_s24le
adts                    hevc                    pcm_s32be
adx                     hls                     pcm_s32le
aea                     iamf                    pcm_s8
aiff                    ico                     pcm_u16be
alp                     ilbc                    pcm_u16le
amr                     image2                  pcm_u24be
amv                     image2pipe              pcm_u24le
apm                     ipod                    pcm_u32be
apng                    ircam                   pcm_u32le
aptx                    ismv                    pcm_u8
aptx_hd                 iterm2                  pcm_vidc
apv                     ivf                     pdv
argo_asf                jacosub                 psp
argo_cvg                jpeg_mpf                rawvideo
asf                     ktx                     rcwt
asf_stream              kvag                    rm
ass                     latm                    roq
ast                     lc3                     rso
astc                    lrc                     rtp
au                      m4v                     rtp_mpegts
avi                     matroska                rtsp
avif                    matroska_audio          sap
avm2                    mcc                     sbc
avs2                    md5                     scc
avs3                    microdvd                segafilm
bit                     mjpeg                   segment
caf                     mkvtimestamp_v2         smjpeg
cavsvideo               mlp                     smoothstreaming
codec2                  mmf                     sox
codec2raw               mov                     spdif
crc                     mp2                     spx
dash                    mp3                     srt
data                    mp4                     stream_segment
daud                    mpeg1system             streamhash
dfpwm                   mpeg1vcd                sup
dirac                   mpeg1video              swf
dnxhd                   mpeg2dvd                tee
dts                     mpeg2svcd               tg2
dv                      mpeg2video              tgp
eac3                    mpeg2vob                truehd
evc                     mpegts                  tta
f4v                     mpjpeg                  ttml
ffmetadata              mxf                     uncodedframecrc
fifo                    mxf_d10                 vc1
filmstrip               mxf_opatom              vc1t
fits                    null                    voc
flac                    nut                     vvc
flv                     obu                     w64
framecrc                oga                     wav
framehash               ogg                     webm
framemd5                ogv                     webm_chunk
g722                    oma                     webm_dash_manifest
g723_1                  opus                    webp
g726                    pcm_alaw                webvtt
g726le                  pcm_f32be               whip
gif                     pcm_f32le               wsaud
gsm                     pcm_f64be               wtv
gxf                     pcm_f64le               wv
h261                    pcm_mulaw               yuv4mpegpipe
h263                    pcm_s16be

Enabled protocols:
async                   httpproxy               rtmps
cache                   https                   rtmpt
concat                  icecast                 rtmpte
concatf                 ipfs_gateway            rtmpts
crypto                  ipns_gateway            rtp
data                    libsrt                  shared
dtls                    libssh                  srtp
fd                      libzmq                  subfile
ffrtmpcrypt             md5                     tcp
ffrtmphttp              mmsh                    tee
file                    mmst                    tls
ftp                     pipe                    udp
gopher                  prompeg                 udplite
gophers                 rtmp
http                    rtmpe

Enabled filters:
a3dscope                dctdnoiz                pan
aap                     ddagrab                 perlin
abench                  deband                  perms
abitscope               deblock                 perspective
acompressor             decimate                phase
acontrast               deconvolve              photosensitivity
acopy                   dedot                   pixdesctest
acrossfade              deesser                 pixelize
acrossover              deflate                 pixscope
acrusher                deflicker               pp7
acue                    deinterlace_d3d12       premultiply
addroi                  deinterlace_qsv         premultiply_dynamic
adeclick                deinterlace_vaapi       prewitt
adeclip                 dejudder                procamp_vaapi
adecorrelate            delogo                  pseudocolor
adelay                  denoise_vaapi           psnr
adenorm                 deshake                 pullup
aderivative             despill                 qp
adrawgraph              detelecine              random
adrc                    dialoguenhance          readeia608
adynamicequalizer       dilation                readvitc
adynamicsmooth          displace                realtime
aecho                   doubleweave             remap
aemphasis               drawbox                 removegrain
aeval                   drawbox_vaapi           removelogo
aevalsrc                drawgraph               repeatfields
aexciter                drawgrid                replaygain
afade                   drawtext                reverse
afdelaysrc              drawvg                  rgbashift
afftdn                  drmeter                 rgbtestsrc
afftfilt                dynaudnorm              roberts
afir                    earwax                  rotate
afireqsrc               ebur128                 rubberband
afirsrc                 edgedetect              sab
aformat                 elbg                    scale
afreqshift              entropy                 scale2ref
afwtdn                  epx                     scale_cuda
agate                   eq                      scale_d3d11
agraphmonitor           equalizer               scale_d3d12
ahistogram              erosion                 scale_qsv
aiir                    estdif                  scale_vaapi
aintegral               exposure                scdet
ainterleave             extractplanes           scharr
alatency                extrastereo             scroll
alimiter                fade                    segment
allpass                 feedback                select
allrgb                  fftdnoiz                selectivecolor
allyuv                  fftfilt                 sendcmd
aloop                   field                   separatefields
alphaextract            fieldhint               setdar
alphamerge              fieldmatch              setfield
amerge                  fieldorder              setparams
ametadata               fillborders             setpts
amf_capture             find_rect               setrange
amix                    firequalizer            setsar
amovie                  flanger                 settb
amplify                 floodfill               sharpness_vaapi
amultiply               format                  shear
anequalizer             fps                     showcqt
anlmdn                  framepack               showcwt
anlmf                   framerate               showfreqs
anlms                   framestep               showinfo
anoisesrc               frc_amf                 showpalette
anull                   freezedetect            showspatial
anullsink               freezeframes            showspectrum
anullsrc                fspp                    showspectrumpic
apad                    fsync                   showvolume
aperms                  gainmap                 showwaves
aphasemeter             gblur                   showwavespic
aphaser                 geq                     shuffleframes
aphaseshift             gfxcapture              shufflepixels
apsnr                   gradfun                 shuffleplanes
apsyclip                gradients               sidechaincompress
apulsator               graphmonitor            sidechaingate
arealtime               grayworld               sidedata
aresample               greyedge                sierpinski
areverse                guided                  signalstats
arls                    haas                    signature
arnndn                  haldclut                silencedetect
asdr                    haldclutsrc             silenceremove
asegment                hdcd                    sinc
aselect                 headphone               sine
asendcmd                hflip                   siti
asetnsamples            highpass                smartblur
asetpts                 highshelf               smptebars
asetrate                hilbert                 smptehdbars
asettb                  histeq                  sobel
ashowinfo               histogram               spectrumsynth
asidedata               hqdn3d                  speechnorm
asisdr                  hqx                     split
asoftclip               hstack                  spp
aspectralstats          hstack_qsv              sr_amf
asplit                  hstack_vaapi            ssim
ass                     hsvhold                 ssim360
astats                  hsvkey                  stereo3d
astreamselect           hue                     stereotools
asubboost               huesaturation           stereowiden
asubcut                 hwdownload              streamselect
asupercut               hwmap                   subtitles
asuperpass              hwupload                super2xsai
asuperstop              hwupload_cuda           superequalizer
atadenoise              hysteresis              surround
atempo                  identity                swaprect
atilt                   idet                    swapuv
atrim                   il                      tblend
avectorscope            inflate                 telecine
avgblur                 interlace               testsrc
avsynctest              interleave              testsrc2
axcorrelate             join                    thistogram
azmq                    kerndeint               threshold
backgroundkey           kirsch                  thumbnail
bandpass                lagfun                  thumbnail_cuda
bandreject              latency                 tile
bass                    latticepal              tiltandshift
bbox                    lenscorrection          tiltshelf
bench                   libvmaf                 tinterlace
bilateral               life                    tlut2
bilateral_cuda          limitdiff               tmedian
biquad                  limiter                 tmidequalizer
bitplanenoise           loop                    tmix
blackdetect             loudnorm                tonemap
blackframe              lowpass                 tonemap_vaapi
blend                   lowshelf                tpad
blockdetect             lumakey                 transpose
blurdetect              lut                     transpose_cuda
bm3d                    lut1d                   transpose_vaapi
boxblur                 lut2                    treble
bwdif                   lut3d                   tremolo
bwdif_cuda              lutrgb                  trim
cas                     lutyuv                  unpremultiply
ccrepack                mandelbrot              unsharp
cellauto                maskedclamp             untile
channelmap              maskedmax               uspp
channelsplit            maskedmerge             v360
chorus                  maskedmin               vaguedenoiser
chromahold              maskedthreshold         varblur
chromakey               maskfun                 vectorscope
chromakey_cuda          mcdeint                 vflip
chromanr                mcompand                vfrdet
chromashift             median                  vibrance
ciescope                mergeplanes             vibrato
codecview               mestimate               vidstabdetect
color                   mestimate_d3d12         vidstabtransform
colorbalance            metadata                vif
colorchannelmixer       midequalizer            vignette
colorchart              minterpolate            virtualbass
colorcontrast           mix                     vmafmotion
colorcorrect            monochrome              volume
colordetect             morpho                  volumedetect
colorhold               movie                   vpp_amf
colorize                mpdecimate              vpp_qsv
colorkey                mptestsrc               vqe_amf
colorlevels             msad                    vstack
colormap                multiply                vstack_qsv
colormatrix             negate                  vstack_vaapi
colorspace              nlmeans                 w3fdif
colorspace_cuda         nnedi                   waveform
colorspectrum           noformat                weave
colortemperature        noise                   xbr
compand                 normalize               xcorrelate
compensationdelay       null                    xfade
concat                  nullsink                xmedian
convolution             nullsrc                 xpsnr
convolve                oscilloscope            xstack
copy                    overlay                 xstack_qsv
corr                    overlay_cuda            xstack_vaapi
cover_rect              overlay_qsv             yadif
crop                    overlay_vaapi           yadif_cuda
cropdetect              owdenoise               yaepblur
crossfeed               pad                     yuvtestsrc
crystalizer             pad_cuda                zmq
cue                     pad_vaapi               zoneplate
curves                  pal100bars              zoompan
datascope               pal75bars               zscale
dblur                   palettegen
dcshift                 paletteuse

Enabled bsfs:
aac_adtstoasc           h264_metadata           pcm_rechunk
ahx_to_mp2              h264_mp4toannexb        pgs_frame_merge
apv_metadata            h264_redundant_pps      prores_metadata
av1_frame_merge         hapqa_extract           remove_extradata
av1_frame_split         hevc_metadata           setts
av1_metadata            hevc_mp4toannexb        showinfo
chomp                   imx_dump_header         smpte436m_to_eia608
dca_core                lcevc_merge             text2movsub
dovi_rpu                lcevc_metadata          trace_headers
dovi_split              media100_to_mjpegb      trim
dts2pts                 mjpeg2jpeg              truehd_core
dump_extradata          mjpega_dump_header      vp9_metadata
dv_error_marker         mov2textsub             vp9_raw_reorder
eac3_core               mpeg2_metadata          vp9_superframe
eia608_to_smpte436m     mpeg4_unpack_bframes    vp9_superframe_split
evc_frame_merge         noise                   vvc_metadata
extract_extradata       null                    vvc_mp4toannexb
filter_units            opus_metadata

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 openal

Enabled outdevs:

git-essentials external libraries' versions: 

AMF v1.5.3
aom v3.15.1-61-g9469625e62
AviSynthPlus v3.7.5-476-g3866da12
cairo 1.18.7
ffnvcodec n13.1.15.0-1-geddcea9
freetype VER-2-14-3
fribidi v1.0.17-4-g24f15ee
gsm 1.0.24
harfbuzz 14.5.1-124-g3c4d303c
lame 3.100
libass 0.17.5-11-gf61db56
libgme 0.6.6
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libssh 0.12.2
libtheora v1.2.0
libwebp v1.6.0-293-ga1d89ff
openal-soft latest
openjpeg2 2.5.4
openmpt libopenmpt-0.6.30-10-g0a3030eb
opus v1.6.1-68-g503d81b1
rubberband v4.0.0
SDL release-2.32.0-259-g4c2d9014a
speex Speex-1.2.1-51-g0589522
srt v1.5.7-11-gb155157
VAAPI 2.25.0.
vidstab v1.1.2-214-ge2445c4
vmaf v3.2.1-36-g0497a0f2
vo-amrwbenc 0.1.3
vorbis v1.3.7-37-g1b75110b
VPL 2.17
vpx v1.17.0-65-g0a6f769e4
x264 v0.165.3223
x265 4.3-56-gea8b761
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.6-253-g67e0603

