require 'rails_helper'

RSpec.describe CclassesController, type: :controller do

  describe "GET #class01" do
    it "returns http success" do
      get :class01
      expect(response).to have_http_status(:success)
    end
  end

end
