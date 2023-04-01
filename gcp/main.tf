# Configure the GCP provider
provider "google" {
  credentials = file("neat-tube-375815-ed168b2bfde9.json")
  project = "neat-tube-375815"
  region  = "us-central1"
}

variable "docker_image" {
  type    = string
  default = "alpine"
}


# Create a new VM instance
resource "google_compute_instance" "vm_instance" {
  name         = "my-vm-instance"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
      size=20
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  metadata = {
      ssh-keys = "ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDJX/D/bCb7Q4n1kcymiN7Hryl+c3BUNzwvE5lBu47AwNPc3ncXR6Jaa/9m0J866rodmC6qEo454p4JZJ50JHWKSHQoKbDYxXSm6hb5WNJpmiZudzoM5GpfPtiqCXIhnLvtUWbkhRdwS/B2YSiDXHYEARAqBCB24ORgFbGWflT819W4AxVm3uHahX6vBs7ryHkedj0idoRtV+3ZKdCZOpNrA9pzedOaNnLvU90lI2Aksf23TUpVEhcuY69oIN1rW1OIguug5lR0i6ckkVZJ0lfMtHlnfsKIbbXobMr55wxUrZBpbnbqPeThMbfwQKeonZVUhfNJPrrzXRLrsOEnFR5eaesnjQ4UVKH7X8goZg2prV9XTi2M4LDgMwsGzJsdlTh+f1hUkr0DIedMfHOBbcvHccnT+FezGcM38uoU/jM2fYI1FdeeNEtG6VDHnObplB+0ssVSBEiRkfKyTXjpVXtV/cVdgFSLvy7KBGc6Jra2h5NkPOD6PXv5ZrGi2dP+hhroRj4acSbViw7bqYaEiFkHyzkVcy1lVfXQHJXrtWFNfqgKWjinoRb3/HoqaA18xljyJx0DQFuj3cc+7q9mkHuaca66sebmdnKuFkOuQYHvBvBYA4W83y33kaVMkI5Q/KMtogNht++ZmCB6kFnXgNUwd/yNlioPtqOFopPQ4+ro0w== example@example.com"

  }

}
