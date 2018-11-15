#!/bin/sh

echo "Content-type: text/html"
echo "Pragma: no-cache"
echo "Cache-Control: max-age=0, no-store, no-cache"
echo ""

# source header.cgi

cat << EOF
<script src="scripts/tab.js" type="text/javascript"></script>
<script src="scripts/motion.js" type="text/javascript"></script>
<style id="custom_css">
#tab_container .container_item {
  display: none;
}

#tab_container .container_item.is-active {
  display: block;
}
</style>

<div class="tabs is-toggle is-fullwidth" id="tab_header">
  <ul>
    <li class="item is-active" data-option="1"><a>General</a></li>
    <li class="item" data-option="2"><a>Video</a></li>
        <li class="item" data-option="3"><a>OSD</a></li>
    <li class="item" data-option="4"><a>Sound</a></li>
    <li class="item" data-option="5"><a>Motion</a></li>
    <li class="item" data-option="6"><a>System Monitor</a></li>
    <li class="item" data-option="7"><a>Theme</a></li>
  </ul>
</div>
<div class="box" id="tab_container">
  <div class="container_item is-active" data-item="1">
    <!-- Date -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>System</p></header>
    <div class='card-content'>
    <form id="tzForm" action="cgi-bin/action.cgi?cmd=settz" method="post">

        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label" for="tz">TZ</label>
            </div>
            <div class="field-body">
                <div class="field">
                    <div class="control">
                        <input class="input" id="tz" name="tz" type="text" size="25" value="$(cat /etc/TZ)" />
                    </div>
                    <p>$(date)</p>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label" for="ntp_srv">NTP Server</label>
            </div>
            <div class="field-body">
                <div class="field">
                    <div class="control">
                        <input class="input" id="ntp_srv" name="ntp_srv" type="text" size="25" value="$(cat /etc/ntp.conf)" />
                    </div>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label" for="hostname">Hostname</label>
            </div>
            <div class="field-body">
                <div class="field">
                <div class="control">
                    <input class="input" id="hostname" name="hostname" type="text" size="15" value="$(hostname)" />
                </div>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
            </div>
            <div class="field-body">
                <div class="field">
                <div class="control">
                    <input id="tzSubmit" class="button is-primary" type="submit" value="Set" />
                </div>
                </div>
            </div>
        </div>
    </form>
    </div>
</div>

<!-- HTTP Password -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>HTTP Password</p></header>
    <div class='card-content'>
        <form id="passwordForm" action="cgi-bin/action.cgi?cmd=set_http_password" method="post">
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label">New Password</label>
            </div>
            <div class="field-body">
                <div class="field">
                    <div class="control">
                        <input class="input" id="password" name="password" type="password" size="12" value="*****"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
            </div>
            <div class="field-body">
                <div class="field">
                <div class="control">
                    <input id="pwSubmit" class="button is-primary" type="submit" value="Set" />
                </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

<!-- Blue / Yellow LED -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>LED</p></header>
    <div class='card-content'>
        <div class="columns">
        <div class="column">
            <label>Blue LED</label>
            <div class="buttons">
                <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=blue_led_on')">On</button>
                <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=blue_led_off')">Off</button>
            </div>
        </div>

        <div class="column">
            <label>Yellow LED</label>
            <div class="buttons">
                <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=yellow_led_on')">On</button>
                <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=yellow_led_off')">Off</button>
            </div>
        </div>

        </div>
    </div>
</div>

<!-- Version -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Version (last commit date from GitHub/autoupdate script)</p></header>
    <div class='card-content'>
    <p>$(cat /opt/version)</p>
    </div>
</div>

  </div>
  <div class="container_item" data-item="2"> 

<!-- IR LED / Cut-->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>IR</p></header>
    <div class='card-content'>
        <div class="columns">
        <div class="column">
            <label>IR LED</label>
            <div class="buttons">
            <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=ir_led_on')">On</button>
            <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=ir_led_off')">Off</button>
            </div>
        </div>

        <div class="column">
            <label>IR Cut</label>
            <div class="buttons">
            <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=ir_cut_on')">On</button>
            <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=ir_cut_off')">Off</button>
            </div>
        </div>
        </div>
    </div>
</div>

<!-- Auto Night Mode -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Auto Night Mode</p></header>
    <div class='card-content'>
        <div class="columns">
        <div class="column">
            <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=auto_night_mode_start')">On</button>
            <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=auto_night_mode_stop')">Off</button>
        </div>
        <div class="column">
        <form id="formldr" action="cgi-bin/action.cgi?cmd=setldravg" method="post">
            <p>Use average measurement on switching.</p>
            <label class="label">Number of measurements</label>
            <div class="field is-grouped">
                <div class="control">
                    <div class="select">
                        <select class="select" name="avg">
                            <option value="1" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 1 ]; then echo selected; fi)>1</option>
                            <option value="2" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 2 ]; then echo selected; fi)>2</option>
                            <option value="3" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 3 ]; then echo selected; fi)>3</option>
                            <option value="4" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 4 ]; then echo selected; fi)>4</option>
                            <option value="5" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 5 ]; then echo selected; fi)>5</option>
                            <option value="10" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 10 ]; then echo selected; fi)>10</option>
                            <option value="15" $(if [ "$(sed s/AVG=// /opt/config/ldr-average.conf)" -eq 15 ]; then echo selected; fi)>15</option>
                        </select>
                    </div>
                </div>
                <p class="control">
                    <input id="ldrSubmit" class="button is-primary" type="submit" value="Set" />
                </p>
            </div>
        </form>
        </div>
        </div>
    </div>
</div>

<!-- RTSP -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>RTSP</p></header>
    <div class='card-content'>
        <div class="columns">

        <div class="column">
            <label>Night Vision</label>
            <div class="buttons">
            <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=toggle-rtsp-nightvision-on')">On</button>
            <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=toggle-rtsp-nightvision-off')">Off</button>
            </div>
        </div>

        <div class="column">
            <label>Flip</label>
            <div class="buttons">
            <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=flip-on')">On</button>
            <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=flip-off')">Off</button>
            </div>
        </div>

        </div>
    </div>
</div>

<!-- Video settings -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Video Settings</p></header>
    <div class='card-content'>
        <form id="formResolution" action="cgi-bin/action.cgi?cmd=set_video_size" method="post">
        <div class="columns">
        <div class="column">
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Video Size</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <div class="select">
                                <select name="video_size">
                                <option value="-W640 -H360" $(if [ "$(cat /opt/config/rtspserver.conf | grep 640)" != "" ]; then echo selected; fi)>640x360</option>
                                <option value="-W960 -H540" $(if [ "$(cat /opt/config/rtspserver.conf | grep 960)" != "" ]; then echo selected; fi)>960x540</option>
                                <option value="-W1280 -H720" $(if [ "$(cat /opt/config/rtspserver.conf | grep 1280)" != "" ]; then echo selected; fi)>1280x720</option>
                                <option value="-W1600 -H900" $(if [ "$(cat /opt/config/rtspserver.conf | grep 1600)" != "" ]; then echo selected; fi)>1600x900</option>
                                <option value="-W1920 -H1080" $(if [ "$(cat /opt/config/rtspserver.conf | grep 1920)" != "" ]; then echo selected; fi)>1920x1080</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Video format</label>
                 </div>
                 <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <div class="select">
                                <select name="video_format">
                                0 = FixedQp, 1 = CBR, 2 = VBR, 3 = SMART
                                <option value="0" $(source /opt/config/rtspserver.conf; if [ "$(echo $VIDEOFORMAT | grep -w 0)" != "" ]; then echo selected; fi)>FixedQp</option>
                                <option value="1" $(source /opt/config/rtspserver.conf; if [ "$(echo $VIDEOFORMAT | grep -w 1)" != "" ]; then echo selected; fi)>CBR</option>
                                <option value="2" $(source /opt/config/rtspserver.conf; if [ "$(echo $VIDEOFORMAT | grep -w 2)" != "" ]; then echo selected; fi)>VBR</option>
                                <option value="3" $(source /opt/config/rtspserver.conf; if [ "$(echo $VIDEOFORMAT | grep -w 3)" != "" ]; then echo selected; fi)>SMART</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="column">
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">bitrate</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <input class="input" id="brbitrate" name="brbitrate" type="text" size="5" value="$(/usr/bin/setconf -g b)"/> kbps
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-body">
                    <div class="field">
                    <div class="control">
                        <input id="resSubmit" class="button is-primary" type="submit" value="Set" />
                    </div>
                    </div>
            </div>
        </div>
        </form>
    </div>
</div>

<!-- H264 RTSP -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Start H264 RTSP</p></header>
    <div class='card-content'>
        <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=h264_start')">Start</button>
        <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=rtsp_stop')">Stop</button>
EOF

PATH="/bin:/sbin:/usr/bin:/media/mmcblk0p2/data/bin:/media/mmcblk0p2/data/sbin:/media/mmcblk0p2/data/usr/bin"

IP=$(ifconfig wlan0 |grep "inet addr" |awk '{print $2}' |awk -F: '{print $2}')
echo "<p>Path to feed : <a href='rtsp://$IP:8554/unicast'>rtsp://$IP:8554/unicast</a></p>"
echo "<p>HLS : <a href='http://$IP:8554/unicast.m3u8'>http://$IP:8554/unicast.m3u8</a></p>"
echo "<p>MPEG-DASH : <a href='http://$IP:8554/unicast.mpd'>http://$IP:8554/unicast.mpd</a></p>"

cat << EOF
    </div>
</div>

<!-- MJPEG RTSP -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Start MJPEG RTSP</p></header>
    <div class='card-content'>
        <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=mjpeg_start')">Start</button>
        <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=rtsp_stop')">Stop</button>
EOF

PATH="/bin:/sbin:/usr/bin:/media/mmcblk0p2/data/bin:/media/mmcblk0p2/data/sbin:/media/mmcblk0p2/data/usr/bin"

IP=$(ifconfig wlan0 |grep "inet addr" |awk '{print $2}' |awk -F: '{print $2}')
echo "<p>Path to feed : <a href='rtsp://$IP:8554/unicast'>rtsp://$IP:8554/unicast</a></p>"

cat << EOF
    </div>
</div>

<!-- Timelapse -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Timelapse</p></header>
    <div class='card-content'>
        <form id="formTimelapse" action="cgi-bin/action.cgi?cmd=conf_timelapse" method="post">
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label">Interval</label>
            </div>
            <div class="field-body">
                <div class="field">
                    <div class="control">
                        <input class="input" id="tlinterval" name="tlinterval" type="text" size="5" value="$(source /opt/config/timelapse.conf && echo "$TIMELAPSE_INTERVAL")"/> seconds
                    </div>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label">Duration</label>
            </div>
            <div class="field-body">
                <div class="field">
                    <div class="control">
                        <input class="input" id="tlduration" name="tlduration" type="text" size="5" value="$(source /opt/config/timelapse.conf && echo "$TIMELAPSE_DURATION")"/> minutes
                    </div>
                    <p class="help">Set to 0 for unlimited</p>
                </div>
            </div>
        </div>
        <div class="field is-horizontal">
            <div class="field-label is-normal">
            </div>
            <div class="field-body">
                <div class="field">
                <div class="control">
                    <input id="tlSubmit" class="button is-primary" type="submit" value="Set" />
                </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

  </div>
  <div class="container_item" data-item="3">

<!-- OSD -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>OSD Display</p></header>
    <div class='card-content'>
        <form id="formOSD" action="cgi-bin/action.cgi?cmd=osd" method="post">

            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Enable Text</label>
                </div>
                <div class="field-body">
                    <div class="field is-grouped">
                        <p class="control">
                            <input type="checkbox" name="OSDenable" value="enabled" $(if [ -f /opt/config/osd.conf ]; then echo checked; fi) />
                        </p>
                        <p class="control">
                            <input class="input" id="osdtext" name="osdtext" type="text" size="25" value="$(source /opt/config/osd.conf && echo "$OSD")"/>
                            <span class="help">
                                Enter time-variables in <a href="http://strftime.org/" target="_blank">strftime</a> format
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Enable Axis</label>
                </div>
                <div class="field-body">
                    <div class="field is-grouped">
                        <p class="control">
                            <input type="checkbox" name="AXISenable" value="enabled" $(if [[ "$(grep DISPLAY_AXIS /opt/config/osd.conf | sed s/DISPLAY_AXIS=//)" == "true" ]];then echo checked; fi) />
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">OSD Color</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <div class="select">
                                <select name="color">
                                <option value="0" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 0 ]; then echo selected; fi)>White</option>
                                <option value="1" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 1 ]; then echo selected; fi)>Black</option>
                                <option value="2" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 2 ]; then echo selected; fi)>Red</option>
                                <option value="3" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 3 ]; then echo selected; fi)>Green</option>
                                <option value="4" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 4 ]; then echo selected; fi)>Blue</option>
                                <option value="5" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 5 ]; then echo selected; fi)>Cyan</option>
                                <option value="6" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 6 ]; then echo selected; fi)>Yellow</option>
                                <option value="7" $(if [ "$(grep COLOR /opt/config/osd.conf | sed s/COLOR=//)" -eq 7 ]; then echo selected; fi)>Purple</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">OSD Text Size</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <div class="select">
                                <select name="size">
                                <option value="0" $(if [ "$(grep SIZE /opt/config/osd.conf | sed s/SIZE=//)" -eq 0 ]; then echo selected; fi)>Small</option>
                                <option value="1" $(if [ "$(grep SIZE /opt/config/osd.conf | sed s/SIZE=//)" -eq 1 ]; then echo selected; fi)>Bigger</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Pixels between chars</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control">
                            <input class="input" id="spacepixels" name="spacepixels" type="number" size="4" value="$(source /opt/config/osd.conf && echo "$SPACE")"/>
                        </p>
                        <p class="help">Can be negative</p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Y Position</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control">
                            <input class="input" id="posy" name="posy" type="number" size="6" value="$(source /opt/config/osd.conf && echo "$POSY")"/>
                        </p>
                    </div>
                </div>
            </div>

            <div class="field is-horizontal">
                <div class="field-label is-normal">
                    <label class="label">Fixed width</label>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <div class="select">
                                <select name="fixedw">
                                <option value="0" $(if [ "$(grep FIXEDW /opt/config/osd.conf | sed s/FIXEDW=//)" -eq 0 ]; then echo selected; fi)>No</option>
                                <option value="1" $(if [ "$(grep FIXEDW /opt/config/osd.conf | sed s/FIXEDW=//)" -eq 1 ]; then echo selected; fi)>Yes</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal">
                <div class="field-label is-normal">
                </div>
                <div class="field-body">
                    <div class="field">
                    <div class="control">
                        <input id="osdSubmit" class="button is-primary" type="submit" value="Set" />
                    </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>

<!-- OSD Debug -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Display debug info on OSD</p></header>
    <div class='card-content'>
        <button class="button is-link" onClick="call('cgi-bin/action.cgi?cmd=onDebug')">On</button>
        <button class="button is-warning" onClick="call('cgi-bin/action.cgi?cmd=offDebug')">Off</button>
    </div>
</div>

  </div>
  <div class="container_item" data-item="4">

<!-- Audio Settings -->
<div class='card status_card'>
    <header class='card-header'>
        <p class='card-header-title'>Audio Settings</p>
    </header>
    <div class='card-content'>
        <form id="formaudioin" action="cgi-bin/action.cgi?cmd=conf_audioin" method="post">
            <div class="columns">
                <div class="column">
                    <div class="field is-horizontal">
                        <div class="field-label is-normal">
                            <label class="label">Select audio format</label>
                        </div>

                        <div class="field-body">
                            <div class="select">
                                <select name="audioinFormat">
                                       <option value="OFF" $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT | grep OFF)" != "" ]; then echo selected; fi)>OFF</option>
                                       <option value="OPUS" $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT | grep OPUS)" != "" ]; then echo selected; fi)>OPUS</option>
                                       <option value="PCM"  $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT | grep -w PCM)" != "" ]; then echo selected; fi)>PCM</option>
                                       <option value="PCMU" $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT | grep -w PCMU)" != "" ]; then echo selected; fi)>PCMU</option>
                                       <option value="MP3-8000" $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT$AUDIOOUTB | grep -w MP38000)" != "" ]; then echo selected; fi)>MP3-8000</option>
                                       <option value="MP3-44100" $(source /opt/config/rtspserver.conf; if [ "$(echo $AUDIOFORMAT$AUDIOOUTBR | grep -w MP344100)" != "" ]; then echo selected; fi)>MP3-44100</option>
                                </select>
                            </div>
                            <span class="help">
                                Needs a restart to become active.
                            </span>
                        </div>
                    </div>
                    <div class="field is-horizontal">
                        <div class="field-label is-normal">
                            <label class="label">Filter (low filter)</label>
                        </div>
                        <div class="field-body">
                            <div class="select">
                                <select name="audioinFilter">
                                       <option value="0" $(if [ "$(/usr/bin/setconf -g q)" == "0" ]; then echo selected; fi)>No filter</option>
                                       <option value="1" $(if [ "$(/usr/bin/setconf -g q)" == "1" ]; then echo selected; fi)>Filter 1</option>
                                       <option value="2" $(if [ "$(/usr/bin/setconf -g q)" == "2" ]; then echo selected; fi)>Filter 2</option>
                                       <option value="3" $(if [ "$(/usr/bin/setconf -g q)" == "3" ]; then echo selected; fi)>NS Filter LOW</option>
                                       <option value="4" $(if [ "$(/usr/bin/setconf -g q)" == "4" ]; then echo selected; fi)>NS Filter MODERATE</option>
                                       <option value="5" $(if [ "$(/usr/bin/setconf -g q)" == "5" ]; then echo selected; fi)>NS Filter HIGH</option>
                                       <option value="6" $(if [ "$(/usr/bin/setconf -g q)" == "6" ]; then echo selected; fi)>NS Filter VERY HIGH</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field is-horizontal">
                        <div class="field-label is-normal">
                            <label class="label">High pass filter</label>
                        </div>
                        <div class="field-body">
                            <p class="control">
                                <input type="checkbox" name="HFEnabled" value="enabled" $(if [ "$(/usr/bin/setconf -g l)" == "true" ]; then echo checked; fi)/>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="column">
                    <div class="field is-horizontal">
                        <div class="field-label is-normal">
                            <label class="label">Volume</label>
                        </div>
                        <input class="slider is-fullwidth" name="audioinVol" step="1" min="-1" max="120" value="$(/usr/bin/setconf -g h)" type="range">
                    </div>
                </div>
            </div>
            <p class="control">
                <input id="audioinSubmit" class="button is-primary" type="submit" value="Set" />
            </p>
        </form>
    </div>
</div>

<!-- Audio / Image -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Tests</p></header>
    <div class='card-content'>

        <div class="columns">
        <div class="column">
            <form id="formAudio" action="cgi-bin/action.cgi?cmd=audio_test" method="post">
                <label>Audio Output Test</label>
                <div class="select">
                    <select name="audioSource">
                        $(
                           for i in `find /usr/share/notify/ -name *.wav`
                           do
                                echo  "<option value=$i> `basename $i` </option>"
                           done
                           for i in `find /usr/share/notify/ -name *.mp3`
                           do
                                echo  "<option value=$i> `basename $i` </option>"
                           done
                        )
                    </select>
                </div>
                <input class="slider is-fullwidth" name="audiotestVol" step="1" min="0" max="120" value="50" type="range">

                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <input id="AudioTestSubmit" class="button is-primary" type="submit" value="Test" />
                        </div>
                    </div>
                </div>
            </form>
        </div>

        <div class="column">
            <label>Image</label>
            <div class="buttons">
                <a class="button is-link" href='cgi-bin/currentpic.cgi' target='_blank'>Get</a>
            </div>
        </div>

        </div>
    </div>
</div>

  </div>

  <div class="container_item" data-item="5">

<!-- Motion Detection -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Motion Detection</p></header>
    <div class='card-content'>
<!-- Use http://odyniec.net/projects/imgareaselect/ -->
<p>
    Select motion detection region.
</p>

<div id="motion_img_container" style="margin: 1em 0; position:relative;">
    <img id="motion_picture" src="cgi-bin/currentpic.cgi" />
    <span id="region_disabled" class="has-text-danger is-size-1" style="display: none; position: absolute; top: 10%; left: 30%; padding: 0.25em 0.5em; background-color: rgba(20, 20, 20, 0.5); border-radius: 0.25em;">
        Region disabled
    </span>
</div>

<div class="column is-two-thirds">
    <form id="confMotionForm" action="cgi-bin/action.cgi?cmd=set_region_of_interest" method="post">
        <input id="x0" name="x0" type="hidden" />
        <input id="y0" name="y0" type="hidden" />
        <input id="x1" name="x1" type="hidden" />
        <input id="y1" name="y1" type="hidden" />
        <input id="restart_server" name="restart_server" type="hidden" />

        <div class="field">
            <label class="label">Region Boundaries</label>
            <div class="control">
                <span id="region_xy"></span>
            </div>
        </div>

        <div class="field">
            <label class="label">Set sensitivity or deactivate</label>
            <div class="control">
                <div class="select">
                    <select name="motion_sensitivity" id="motion_sensitivity">
                        <option value="-1">Motion deactivated</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="field">
            <label class="label">Display motion indicator if motion is detected</label>
            <div class="control">
                <div class="select">
                    <select name="motion_indicator_color" id="motion_indicator_color">
                        <option value="-1">Deactivated</option>
                        <option value="0">White</option>
                        <option value="1">Black</option>
                        <option value="2">Red</option>
                        <option value="3">Green</option>
                        <option value="4">Blue</option>
                        <option value="5">Cyan</option>
                        <option value="6">Yellow</option>
                        <option value="7">Purple</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="field">
            <div class="control">
                <label class="checkbox">
                    <input type="checkbox" name="motion_tracking" id="motion_tracking" onchange="setTracking(this, false)"> Enable motion tracking (when enabled no region of interest is no more used)
                </label>
            </div>
        </div>

        <div class="field">
            <label class="label">Motion Timeout</label>
            <div class="control">
                <input class="input" id="motion_timeout" name="motion_timeout" type="number" size="6">
            </div>
            <p class="help">Restore camera position after x seconds, -1 to deactivate</p>
        </div>
        <div class="field">
            <div class="control">
                <input id="configMotionSubmit" class="button is-primary" type="submit" value="Configure motion" />
            </div>
        </div>
    </form>
</div>
    </div>
</div>

<!-- Motor -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Motor</p></header>
    <div class='card-content'>
        <table class="motor_control">
            <tr>
                <td></td>
                <td>
                    <button class="button is-link" onclick="call('cgi-bin/action.cgi?cmd=motor_up&val='+document.getElementById('val').value)">&uarr; Up</button>
                </td>
                <td></td>
            </tr>
            <tr>
                <td>
                    <button class="button is-link" onclick="call('cgi-bin/action.cgi?cmd=motor_left&val='+document.getElementById('val').value)">&larr; Left</button>
                </td>
                <td>
                    <input class="input has-text-centered" type="text" id="val" name="val" value="100">
                </td>
                <td>
                    <button class="button is-link" onclick="call('cgi-bin/action.cgi?cmd=motor_right&val='+document.getElementById('val').value)">Right &rarr;</button>
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <button class="button is-link" onclick="call('cgi-bin/action.cgi?cmd=motor_down&val='+document.getElementById('val').value)">&darr; Down</button>
                </td>
                <td></td>
            </tr>
        </table>
        <div class="buttons">
        <button class="button is-warning" onclick="call('cgi-bin/action.cgi?cmd=motor_vcalibrate')">Calibrate Vertical</button>
        <button class="button is-warning" onclick="call('cgi-bin/action.cgi?cmd=motor_hcalibrate')">Calibrate Horizontal</button>
        </div>
    </div>
</div>

  </div>

  <div class="container_item" data-item="6">

<!-- System controls -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Actions</p></header>
    <div class='card-content'>
<button class="button" onclick="call('cgi-bin/action.cgi?cmd=shutdown')">Shutdown</button>
    </div>
</div>

<!-- Process List -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Process List</p></header>
    <div class='card-content'>
        <pre>$(ps)</pre>
    </div>
</div>

<!-- Mount Points -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Mount Points</p></header>
    <div class='card-content'>
        <pre>$(mount)</pre>
    </div>
</div>

EOF
source func.cgi
if [ -e "/etc/fang_hacks.cfg" ]; then source /etc/fang_hacks.cfg; fi
PATH="/bin:/sbin:/usr/bin:/system/bin"

cat << EOF
<!-- Network Information -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Network Information</p></header>
    <div class='card-content'>
        <pre>Interfaces:<br/>$(ifconfig; iwconfig)</pre>
        <pre>Routes:<br/>$(route)</pre>
        <pre>DNS:<br/>$(cat /etc/resolv.conf)</pre>
    </div>
</div>


  </div>

  <div class="container_item" data-item="7">

<!-- Change Theme -->
<div class='card status_card'>
    <header class='card-header'><p class='card-header-title'>Network Information</p></header>
    <div class='card-content'>
                        <div class="dropdown-content">
                            <a id="theme_choice_0" href="javascript: setTheme('0')" class="theme_choice dropdown-item" data-css="css/bulma.0.6.2.min.css">
                                Light
                            </a>
                            <a id="theme_choice_1" href="javascript: setTheme('1')" class="theme_choice dropdown-item" data-css="https://cdn.jsdelivr.net/npm/bulmaswatch@0.6.2/slate/bulmaswatch.min.css">
                                Dark
                            </a>
<a id="theme_choice_2" href="javascript: setTheme('2')" class="theme_choice dropdown-item" data-css="css/bulma-flat.min.css">
                                Flat
                            </a>
<a id="theme_choice_3" href="javascript: setTheme('3')" class="theme_choice dropdown-item" data-css="css/bulma-flatty-nm.min.css">
                                Flaty Night
                            </a>
                        </div>
    </div>
</div>

  </div>

</div>




<script>
    function call(url){
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.send();
    }

</script>


EOF
script=$(cat /var/www/scripts/status.cgi.js)
echo "<script>$script</script>"
