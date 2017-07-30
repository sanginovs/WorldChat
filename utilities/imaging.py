from wand.image import Image
import os
import boto3
from boto3.s3.transfer import S3Transfer


from utilities.common import utc_timestamp as now  
from settings import UPLOAD_FOLDER, AWS_BUCKET

def thumbnail_process(file, content_type, content_id, sizes=[("sm", 50), ("lg", 75), ("xlg", 200)]):
    '''pass a file, content type, id, and 3 sizes'''
   
    image_id = now()  #timestamp
     #content_id is user id
    filename_template = content_id + '.%s.%s.png'   
    
    # original
    with Image(filename=file) as img:
        crop_center(img)  #selects the center of the image
        img.format = 'png'
        #we move this to upload folder and merge it with content type, 
        img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')))
        
    # sizes
    for (name, size) in sizes:
        with Image(filename=file) as img:
            crop_center(img)
            img.sample(size, size)
            img.format = 'png'
            img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, name)))
    #if aws_bucket exist then store image files inside it        
    if AWS_BUCKET:
        s3 = boto3.client('s3') #initialize s3 client
        transfer = S3Transfer(s3) #initialize transfer client
        transfer.upload_file(
            os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')), 
            AWS_BUCKET, 
            os.path.join(content_type, filename_template % (image_id, 'raw')),
            extra_args={'ACL': 'public-read', 'ContentType': 'image/png'}
            )
        os.remove(os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')))
    
        for (name, size) in sizes:
            #for size we upload them in S3 bucket
            transfer.upload_file(
                os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, name)), 
                AWS_BUCKET, 
                os.path.join(content_type, filename_template % (image_id, name)),
                extra_args={'ACL': 'public-read', 'ContentType': 'image/png'}
                ) #extra args is rules so anyone is able to read those files
            os.remove(os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, name)))
            #remove from local server
    #delete original file
    os.remove(file)
    return image_id
    #we will have 3 files .sm .lg. xlg
    
def crop_center(image):
    '''tries to get if the image is taller than wider, if it is, it gets that measurement
    else, it gets width and divides it by two
    '''
    dst_landscape = 1 > image.width / image.height
    wh = image.width if dst_landscape else image.height
    image.crop(
        left=int((image.width - wh) / 2),
        top=int((image.height - wh) / 2),
        width=int(wh),
        height=int(wh)
    )