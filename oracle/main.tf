provider "oci" {
  # Replace with your own authentication details
  tenancy_ocid     = "ocid1.tenancy.oc1..aaaaaaaa3buw5rphispxszgpp4lg5na2owmm72q67kim4g5mailn3u3sukla"
  user_ocid        = "ocid1.user.oc1..aaaaaaaalwatkhvzgaurhbaenmbgkep54hl2v2khkcqncg4sahrlgpoci7lq"
  fingerprint      = "e9:df:e3:89:25:7e:49:63:75:f6:2d:a0:f4:0f:61:78"
  private_key_path = "private.pem"
  region           = "ca-toronto-1"
}

variable "docker_image" {
  type    = string
  default = "alpine"


}

data "oci_identity_availability_domains" "test_availability_domains" {
    #Required
    compartment_id = "ocid1.tenancy.oc1..aaaaaaaa3buw5rphispxszgpp4lg5na2owmm72q67kim4g5mailn3u3sukla"
}

resource "oci_core_instance" "example_instance" {
  # Replace with your own values
  compartment_id = "ocid1.tenancy.oc1..aaaaaaaa3buw5rphispxszgpp4lg5na2owmm72q67kim4g5mailn3u3sukla"
  availability_domain = data.oci_identity_availability_domains.test_availability_domains.availability_domains.0.name
  shape = "VM.Standard.E2.1.Micro"
  display_name = "example_instance"
  subnet_id = "ocid1.subnet.oc1.ca-toronto-1.aaaaaaaamsotegmgc47oufhz367fiocmzf5huk2dend573xx7dyjz47ibbga"
  metadata = {
    ssh_authorized_keys = <<-EOT
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDJX/D/bCb7Q4n1kcymiN7Hryl+c3BUNzwvE5lBu47AwNPc3ncXR6Jaa/9m0J866rodmC6qEo454p4JZJ50JHWKSHQoKbDYxXSm6hb5WNJpmiZudzoM5GpfPtiqCXIhnLvtUWbkhRdwS/B2YSiDXHYEARAqBCB24ORgFbGWflT819W4AxVm3uHahX6vBs7ryHkedj0idoRtV+3ZKdCZOpNrA9pzedOaNnLvU90lI2Aksf23TUpVEhcuY69oIN1rW1OIguug5lR0i6ckkVZJ0lfMtHlnfsKIbbXobMr55wxUrZBpbnbqPeThMbfwQKeonZVUhfNJPrrzXRLrsOEnFR5eaesnjQ4UVKH7X8goZg2prV9XTi2M4LDgMwsGzJsdlTh+f1hUkr0DIedMfHOBbcvHccnT+FezGcM38uoU/jM2fYI1FdeeNEtG6VDHnObplB+0ssVSBEiRkfKyTXjpVXtV/cVdgFSLvy7KBGc6Jra2h5NkPOD6PXv5ZrGi2dP+hhroRj4acSbViw7bqYaEiFkHyzkVcy1lVfXQHJXrtWFNfqgKWjinoRb3/HoqaA18xljyJx0DQFuj3cc+7q9mkHuaca66sebmdnKuFkOuQYHvBvBYA4W83y33kaVMkI5Q/KMtogNht++ZmCB6kFnXgNUwd/yNlioPtqOFopPQ4+ro0w== example@example.com
    EOT
  }

  source_details {
    source_type = "image"
    source_id = "ocid1.image.oc1.ca-toronto-1.aaaaaaaaybil2cgxoj2lq5nuxquiuy3efqcgi673htzptsdmbasvtrwm7sra"
  }

}

