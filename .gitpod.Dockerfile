FROM gitpod/workspace-base

# Install pyenv dependencies
USER root
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl

USER gitpod

# Install pyenv
RUN curl https://pyenv.run | bash

# Add pyenv to PATH and initialize
ENV PATH="/home/gitpod/.pyenv/bin:/home/gitpod/.pyenv/shims:$PATH"
RUN echo 'export PATH="/home/gitpod/.pyenv/bin:/home/gitpod/.pyenv/shims:$PATH"' >> /home/gitpod/.bashrc
RUN echo 'eval "$(pyenv init --path)"' >> /home/gitpod/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> /home/gitpod/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> /home/gitpod/.bashrc

# Install Python 3.12.4 using pyenv
RUN bash -c "source /home/gitpod/.bashrc && pyenv install 3.12.4 && pyenv global 3.12.4"

# Verify Python installation
RUN bash -c "source /home/gitpod/.bashrc && python3 --version"

# Install nilup, add to PATH, and verify installation in one RUN command
RUN curl -sS https://nilup.nilogy.xyz/install.sh | bash && \
    export PATH=$PATH:/home/gitpod/.nilup/sdks/latest:/home/gitpod/.nilup/bin && \
    bash -c "source /home/gitpod/.bashrc && nilup -V"