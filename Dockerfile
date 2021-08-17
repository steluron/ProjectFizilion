 # inherit prebuilt image
FROM prajwals3/projectfizilion:latest

# env setup
RUN mkdir /Fizilion && chmod 777 /Fizilion
ENV PATH="/Fizilion/bin:$PATH"
WORKDIR /Fizilion

# clone repo
RUN git clone https://https://github.com/FrostSue/ProjectFizilion -b Demon /Fizilion
#RUN git clone https://github.com/Senpai-sama-afk/ProjectFizilion -b dragon /Fizilion

# Copies session and config(if it exists)
COPY ./sample_config.env ./userbot.session* ./config.env* /Fizilion/

# install required pypi modules
RUN pip3 install -r requirements.txt

# Finalization
CMD ["python3","-m","userbot"]
