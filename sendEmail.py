import pandas as pd
import time

def send_email(se_from, se_pwd, se_to, se_subject, se_plain_text='', se_html_text='', se_attachments=[]):
    """ Send an email with the specifications in parameters

    The following youtube channel helped me a lot to build this function:
    https://www.youtube.com/watch?v=JRCJ6RtE3xU
    How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More
    Corey Schafer youtube channel

    Input:
        se_from : email address that will send the email
        se_pwd : password for authentication (uses SMTP.SSL for authentication)
        se_to : destination email. For various emails, use ['email1@example.com', 'email2@example.com']
        se_subject : email subject line
        se_plain_text : body text in plain format, in case html is not supported
        se_html_text : body text in html format
        se_attachments : list of attachments. For various attachments, use ['path1\file1.ext1', 'path2\file2.ext2', 'path3\file3.ext3']. Follow your OS guidelines for directory paths. Empty list ([]) if no attachments

    Returns
    -------
        se_error_code : returns True if email was successful (still need to incorporate exception handling routines)
    """

    import smtplib
    from email.message import EmailMessage

    # Join email parts following smtp structure
    msg = EmailMessage()
    msg['From'] = se_from
    msg['To'] = se_to
    msg['Subject'] = se_subject
    msg.set_content(se_plain_text)
    # Adds the html text only if there is one
    if se_html_text != '':
        msg.add_alternative("""{}""".format(se_html_text), subtype='html')

    # Checks if there are files to be sent in the email
    if len(se_attachments) > 0:
        # Goes through every file in files list
        for file in se_attachments:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            # Attaches the file to the message. Leaves google to detect the application to open it
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Sends the email that has been built
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(se_from, se_pwd)
        smtp.send_message(msg)

    return True

if __name__=='__main__':

    html = """<!DOCTYPE html><html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"><head><title></title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"><style>*{box-sizing: border-box;}body{margin: 0;padding: 0;}a[x-apple-data-detectors]{color: inherit !important;text-decoration: inherit !important;}#MessageViewBody a{color: inherit;text-decoration: none;}p{line-height: inherit}@media (max-width:700px){.fullMobileWidth,.row-content{width: 100% !important;}.image_block img.big{width: auto !important;}.column .border{display: none;}.video_block .sizer{max-width: none !important;}table{table-layout: fixed !important;}.stack .column{width: 100%;display: block;}}</style></head><body style="background-color: #141414; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;"><table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #141414;"><tbody><tr><td><table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #470780;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="paragraph_block" width="100%" border="0" cellpadding="15" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td><div style="color:#ffd700;direction:ltr;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-size:29px;font-weight:700;letter-spacing:0px;line-height:120%;text-align:center;"><p style="margin: 0;">Voting Beings Now!!!</p></div></td></tr></table><table class="button_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="text-align:center;"><div align="center"><a href="https://engage.nyu.edu/" target="_blank" style="text-decoration:none;display:inline-block;color:#0d0c0c;background-color:#f9f0f9;border-radius:9px;width:auto;border-top:1px solid #8a3b8f;border-right:1px solid #8a3b8f;border-bottom:1px solid #8a3b8f;border-left:1px solid #8a3b8f;padding-top:5px;padding-bottom:5px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:15px;padding-right:15px;font-size:12px;display:inline-block;letter-spacing:normal;"><span style="font-size: 12px; line-height: 2; word-break: break-word; mso-line-height-alt: 24px;"><strong>Cast Your Vote Here</strong></span></span></a></div></td></tr></table><table class="heading_block" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td><h3 style="margin: 0; color: #eff1f6; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 41px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">&nbsp; UTKARSHA FOR PRESIDENT</span></h3></td></tr></table><table class="heading_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="text-align:center;width:100%;"><h1 style="margin: 0; color: #ff69b4; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Elevation Through Inclusion</span></h1></td></tr></table><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;"><div align="center" style="line-height:10px"><img class="fullMobileWidth big" src="http://www.swaroopmanchala.com/static/img/huge/0001.jpg" style="display: block; height: auto; border: 0; width: 510px; max-width: 100%;" width="510" alt="Helping Hand" title="Helping Hand"></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0002.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608026" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407156737-6e7ddf88874886f86bc010bf8e7b9e552bf50bbe5f0e282034eefd0e282ddc72-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407156737-6e7ddf88874886f86bc010bf8e7b9e552bf50bbe5f0e282034eefd0e282ddc72-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0003.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608055" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407156817-b0045107015d8e9bb53fc7b670b19904f6a511cd32e2b6884fa1bd2a85ed9f8b-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407156817-b0045107015d8e9bb53fc7b670b19904f6a511cd32e2b6884fa1bd2a85ed9f8b-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0004.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608087" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407156880-7d10e3817ccda0076d4feca7f2ccc4a7b811f75789371e67758fdb73850b9320-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407156880-7d10e3817ccda0076d4feca7f2ccc4a7b811f75789371e67758fdb73850b9320-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0005.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608117" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407157097-bd9925e793cf72ce0880f9b131073f95f92d5ed8864b2b5307f8a749909da750-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407157097-bd9925e793cf72ce0880f9b131073f95f92d5ed8864b2b5307f8a749909da750-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0006.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608153" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407157019-b37ecbe0064f6ca25dd5d624091e9cd26d0a54714038df9ea0f416c2ed8b32be-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407157019-b37ecbe0064f6ca25dd5d624091e9cd26d0a54714038df9ea0f416c2ed8b32be-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #490790; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;"><div align="center" style="line-height:10px"><img src="http://www.swaroopmanchala.com/static/img/huge/0007.jpg" style="display: block; height: auto; border: 0; width: 340px; max-width: 100%;" width="340" alt="I'm an image" title="I'm an image"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="video_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr style="box-sizing: content-box;"><td style="box-sizing: content-box; width: 100%; padding-left: 0; padding-right: 0; padding-top: 5px; padding-bottom: 5px;" width="100%"><div class="sizer" align="center" style="box-sizing: content-box; max-width: 340px; min-width: 320px;"><a class="video-preview" href="https://vimeo.com/695608196" target="_blank" style="box-sizing: content-box; background-color: #5b5f66; background-image: radial-gradient(circle at center, #5b5f66, #1d1f21); display: block; text-decoration: none;"><div style="box-sizing: content-box;"><table cellpadding="0" cellspacing="0" border="0" width="100%" background="https://i.vimeocdn.com/video/1407156993-4b40150dcafe6abaa791534a8dae821d00e5e6d299e5db47b76e159065566c66-d_640" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; box-sizing: content-box; background-image: url(https://i.vimeocdn.com/video/1407156993-4b40150dcafe6abaa791534a8dae821d00e5e6d299e5db47b76e159065566c66-d_640); background-size: cover; min-height: 240px; min-width: 320px;"><tr style="box-sizing: content-box;"><td width="25%" style="box-sizing: content-box;"><img src="https://beefree.io/img-host/video_ratio_4-3.gif" alt="ratio" width="100%" border="0" style="display: block; box-sizing: content-box; height: auto; opacity: 0; visibility: hidden;"></td><td width="50%" align="center" valign="middle" style="box-sizing: content-box; vertical-align: middle;"><div class="play-button_outer" style="box-sizing: content-box; display: inline-block; vertical-align: middle; background-color: #ffffff; border: 3px solid #ffffff; height: 59px; width: 59px; border-radius: 100%;"><div style="box-sizing: content-box; padding: 14.75px 22.69230769230769px;"><div class="play-button_inner" style="box-sizing: content-box; border-style: solid; border-width: 15px 0 15px 20px; display: block; font-size: 0; height: 0; width: 0; border-color: transparent transparent transparent #000000;">&#160;</div></div></div></td><td width="25%" style="box-sizing: content-box;">&#160;</td></tr></table></div></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680"><tbody><tr><td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="button_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:15px;text-align:center;"><div align="center"><a href="https://engage.nyu.edu/" target="_blank" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#8a3b8f;border-radius:4px;width:auto;border-top:1px solid #8a3b8f;border-right:1px solid #8a3b8f;border-bottom:1px solid #8a3b8f;border-left:1px solid #8a3b8f;padding-top:5px;padding-bottom:5px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;">Vote Here !!</span></span></a></div></td></tr></table></td><td class="column column-2" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="social_block" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:15px;text-align:center;"><table class="social-table" width="144px" border="0" cellpadding="0" cellspacing="0" role="presentation" align="center" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td style="padding:0 2px 0 2px;"><a href="https://www.facebook.com/utkarsha.chourasiya.9" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" width="32" height="32" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 2px 0 2px;"><a href="https://www.linkedin.com/in/utkarsha-chourasia/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/linkedin@2x.png" width="32" height="32" alt="Linkedin" title="linkedin" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 2px 0 2px;"><a href="https://www.instagram.com/raghvie/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" width="32" height="32" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 2px 0 2px;"><a href="mailto:uc2012@nyu.edu" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/mail@2x.png" width="32" height="32" alt="E-Mail" title="E-Mail" style="display: block; height: auto; border: 0;"></a></td></tr></table></td></tr></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></body></html>"""
    data = pd.read_csv('Emails.csv')
    #data = pd.read_csv('sample.csv')
    i = 0

    for index, row in data.iterrows():
        print(row['EMAIL'])
        i = i +1
        print(i)
        try:
            if send_email('utkarshac13sia@gmail.com','Utkarsha@13',row['EMAIL'],'Vote Now!! Graduate Student Council Elections','',html):
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(str(e))
            time.sleep(250)


